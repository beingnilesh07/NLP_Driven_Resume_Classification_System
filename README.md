# 📄 NLP_Driven_Resume_Classification_System

## 📌 Project Overview

This project builds a machine learning system that can automatically
classify resumes into different job roles based on their content.
Recruiters often receive a large number of resumes for a single
position, and reviewing each one manually can be time‑consuming. The
purpose of this project is to simplify that process by analyzing resume
text and predicting the most relevant job category.

The system uses Natural Language Processing (NLP) techniques along with
machine learning models to understand the content of resumes.

------------------------------------------------------------------------

## Problem Statement

In traditional hiring workflows, HR teams manually read resumes to
determine whether a candidate is suitable for a role. This approach
becomes inefficient when the number of applications is high.

This project aims to automate the resume screening process by building a
model that can analyze resume text and classify it into the correct job
domain.

------------------------------------------------------------------------

## 🎯 Project Objective

-   Automatically classify resumes into job categories
-   Reduce manual screening time for recruiters
-   Apply NLP techniques for text processing
-   Build and deploy a machine learning model

------------------------------------------------------------------------

## 📂 Dataset

The dataset consists of resumes along with their corresponding job
categories.

Typical information present in the dataset: - Resume text - Job category
label

Resumes generally contain information such as: - Skills - Education -
Work experience - Tools and technologies

------------------------------------------------------------------------

## Data Preprocessing

Before training the model, the resume text is cleaned and prepared.

Steps performed: - Converting text to lowercase - Removing punctuation
and special characters - Removing stopwords - Tokenization - Converting
text into numerical vectors

------------------------------------------------------------------------

## Feature Extraction

The text data is converted into numerical format using:

**TF‑IDF (Term Frequency -- Inverse Document Frequency)**

TF‑IDF highlights important words in each resume while reducing the
importance of commonly used words.

------------------------------------------------------------------------

## Machine Learning Model

Common models suitable for this problem include:

-   Naive Bayes
-   Logistic Regression
-   Support Vector Machine (SVM)

In this project, the model is trained using TF‑IDF features extracted
from resume text.

------------------------------------------------------------------------

## Model Evaluation

The model is evaluated using:

-   Accuracy
-   Precision
-   Recall
-   F1 Score

These metrics help measure how well the model classifies resumes into
the correct categories.

------------------------------------------------------------------------

## 🚀 Deployment using Streamlit

To make the model easy to use, a simple web application is created using
**Streamlit**.

The Streamlit app allows users to: 
1. Upload or paste a resume 
2. Process the text
3. Predict the job category using the trained model
4. Display the predicted result

This makes the project interactive and easier to demonstrate.

Run the Streamlit application:

streamlit run app.py

------------------------------------------------------------------------

## Technologies Used

-   Python
-   Pandas
-   NumPy
-   Scikit‑learn
-   NLP techniques
-   TF‑IDF Vectorizer
-   Streamlit
-   Jupyter Notebook

## Future Improvements

Possible improvements include:

-   Using deep learning models such as BERT/Tranformers
-   Adding resume ranking functionality
-   Deploying the model on a cloud platform
-   Integrating with recruitment portals

------------------------------------------------------------------------

## Conclusion

This project demonstrates how machine learning and natural language
processing can automate the resume screening process. By classifying
resumes automatically, recruiters can focus on evaluating the most
relevant candidates.

------------------------------------------------------------------------
