📦 E-Commerce Delivery Time Prediction

Powered by Machine Learning • Built with ❤️

🚀 Project Overview

This project predicts whether an e-commerce order will be delivered on time based on customer, product, and shipment-related attributes.
It is an end-to-end Machine Learning project, covering:

📊 Data preprocessing & feature engineering

🤖 Model training with hyperparameter tuning

🧠 Best model selection based on F1-score

🌐 Deployment using Streamlit with a modern UI

🎯 Problem Statement

Late deliveries negatively impact customer satisfaction and business reputation.
The goal of this project is to predict delivery delays in advance, enabling businesses to take proactive actions.

🧠 Machine Learning Approach

Task Type: Binary Classification

Target Variable: Reached.on.Time_Y.N

Evaluation Metric: F1 Score (handles class imbalance effectively)

🔍 Models Trained

Logistic Regression

Random Forest

Gradient Boosting

Support Vector Classifier (SVC)

XGBoost (Best Performing Model)

All models are trained using GridSearchCV for fair and optimized comparison.

🗂️ Project Structure
📦 E-Commerce Delivery Time Prediction

Powered by Machine Learning • Built with ❤️

🚀 Project Overview

This project predicts whether an e-commerce order will be delivered on time based on customer, product, and shipment-related attributes.
It is an end-to-end Machine Learning project, covering:

📊 Data preprocessing & feature engineering

🤖 Model training with hyperparameter tuning

🧠 Best model selection based on F1-score

🌐 Deployment using Streamlit with a modern UI

🎯 Problem Statement

Late deliveries negatively impact customer satisfaction and business reputation.
The goal of this project is to predict delivery delays in advance, enabling businesses to take proactive actions.

🧠 Machine Learning Approach

Task Type: Binary Classification

Target Variable: Reached.on.Time_Y.N

Evaluation Metric: F1 Score (handles class imbalance effectively)

🔍 Models Trained

Logistic Regression

Random Forest

Gradient Boosting

Support Vector Classifier (SVC)

XGBoost (Best Performing Model)

All models are trained using GridSearchCV for fair and optimized comparison.

🗂️ Project Structure
E-Commerce_product/
│
├─ app.py                     # Streamlit web application
├─ src/
│   └─ config.py              # Central configuration file
├─ models/
│   ├─ best_model.joblib      # Final trained model
│   └─ feature_list.json      # Feature alignment for inference
├─ notebooks/
│   ├─ eda.ipynb              # Exploratory Data Analysis
│   ├─ preprocessing.ipynb    # Data preprocessing pipeline
│   └─ training.ipynb         # Model training & evaluation
├─ data/                      # Dataset (optional for deployment)
├─ requirements.txt           # Project dependencies
├─ .gitignore
└─ README.md

⚙️ Tech Stack

Programming Language: Python 🐍

Data Analysis: Pandas, NumPy

Machine Learning: Scikit-Learn, XGBoost

Model Persistence: Joblib

Web App: Streamlit

IDE: VS Code

🌐 Web Application Features

🖤 Modern Black & Yellow UI

📝 Interactive input form

🔮 Real-time prediction

📊 Prediction confidence (probability)

💼 Business-friendly output messages
