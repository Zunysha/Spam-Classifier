# Spam Detection Flask App  
  
This repository contains a Flask web application for detecting spam messages using a trained Random Forest model and TF-IDF vectorization.  
  
## Table of Contents  
- [Spam Detection Flask App](#spam-detection-flask-app)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [How to use](#how-to-use)
  
## Introduction  
  
This project is a simple web application built using Flask. It allows users to input a text message and predict whether it is spam or not using a pre-trained Random Forest model. The model uses TF-IDF vectorization for text feature extraction.  
  
## Features  
  
- Input text message for spam detection.  
- Preprocesses the text message and extracts relevant features.  
- Uses a trained Random Forest model to predict if the message is spam.  
- Displays the prediction result on the web page.  
  
## How to use
- Clone the repository.
- Run the app.py file in app folder.
- Click on the link to folllow the server the app is running on.
- Enter the text you want to classify.
- Click on classify.


Model Training
 
The model was trained on the SMSSpamCollection dataset. The training process includes the following steps:

Load and preprocess the dataset.
Extract features such as text length and punctuation percentage.
Use TF-IDF vectorization for text feature extraction.
Train a Random Forest model using the extracted features.
Save the trained model and vectorizer for future use.

The SMSSpamCollection dataset contains labeled SMS messages that are categorized as either spam or ham (not spam). The preprocessing steps include cleaning the text, removing stopwords, and stemming.
Acknowledgements
 

The dataset used for training the model is the SMSSpamCollection dataset.
The Flask framework for creating the web application.
The NLTK library for natural language processing tasks.
Scikit-learn for machine learning and data processing.