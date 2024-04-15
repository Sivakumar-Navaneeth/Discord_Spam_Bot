import pandas as pd
import numpy as np
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

def process(msg):
    nopunc = [c for c in msg if c not in string.punctuation]
    nopunc=''.join(nopunc)
    return [w for w in nopunc.split() if w.lower() not in stopwords]

def check_spam(to_pred):
    data=pd.read_csv("spam.csv" , sep=",", encoding='latin-1' , names=["label","message","a","aa","sa"])
    data=data.drop(0).dropna(axis=1)
    data['length'] = data['message'].apply(len)

    bow_transformer = CountVectorizer(analyzer=process).fit(data['message'])
    data_bow=bow_transformer.transform(data['message'])

    tfidf_transformer=TfidfTransformer().fit(data_bow)
    data_tfidf=tfidf_transformer.transform(data_bow)

    spam_detect_model = MultinomialNB().fit(data_tfidf,data['label'])

    msg_train,msg_test,label_train,label_test = train_test_split(data['message'],data['label'],test_size=0.3,random_state=42)

    pipeline = Pipeline([
        ( 'bow',CountVectorizer(analyzer=process)),
        # ('tfidf',TfidfTransformer()),
        ('classifier',MultinomialNB()),
    ])

    pipeline.fit(msg_train,label_train)
    predictions = pipeline.predict(msg_test)
    
    
    pred=pipeline.predict([to_pred])
    print("THE MESSAGE: ",to_pred,"\nis ",pred[0])
    return(pred[0])

if __name__ == '__main__':
    print(check_spam(""))