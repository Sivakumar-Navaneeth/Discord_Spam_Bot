# Discord Spam Detection

This project aims to predict spam messages in a social messaging platform named Discord.

## Table of Contents

- [Purpose](#purpose)
- [Technologies and Libraries](#technologies-and-libraries)
- [Data Sources](#data-sources)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Results](#results)
- [Contributors](#contributors)
- [Future Work](#future-work)

## Purpose

The purpose of this project is to detect and filter out spam messages on Discord to improve the user experience and maintain the integrity of communication on the platform.

## Technologies and Libraries

- Python
- Scikit-learn
- Pandas
- Numpy

### Models

- Count Vectorizer
- TFIDF Transform
- Multinomial Naive Bayes Algorithm

## Data Sources

This dataset contains the spam and ham messages used for the purpose of spam classification. This dataset is taken from UCI machine learning repository. The dataset can be in CSV format with at least two columns: `message` and `label`.

## Setup and Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/discord-spam-detection.git
    cd discord-spam-detection
    ```

2. Create and activate a conda environment:

    ```bash
    conda create --name discord-spam-detection python=3.8
    conda activate discord-spam-detection
    ```

3. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

4. Add your Discord bot token in the configuration file (e.g., `config.py`):

    ```python
    SECOND_BOT_TOKEN = 'your-discord-bot-token-here'
    ```

## Usage

1. Train the model:

    ```bash
    python spam.py
    ```

    This script will train the Count Vectorizer, TFIDF Transform, and Multinomial Naive Bayes Algorithm on your dataset and save the model.

2. Run the bot:

    ```bash
    python discord_bot.py
    ```

    This script will start the Discord bot, which will use the trained model to predict and filter spam messages in real-time.

## Results

The performance of the spam detection model can be evaluated using metrics such as accuracy, precision, recall, and F1-score.

## Contributors

- [Navaneeth Sivakumar](https://github.com/Sivakumar-Navaneeth)

## Future Work

- Enhance the model with more advanced techniques like deep learning.
- Collect and use a larger dataset to improve accuracy.
- Implement real-time feedback and retraining mechanism.

---
