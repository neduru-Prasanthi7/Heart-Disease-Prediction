# Heart-Disease-Prediction
#  Heart Disease Prediction

## 📌 Project Overview
This project predicts the **risk of heart disease** using multiple **machine learning classification algorithms**.  
The implementation follows a **modular approach using classes, objects, and functions**, ensuring clean and reusable code.

Multiple models were trained and evaluated, and the **best model was selected using ROC–AUC analysis**.  
Finally, the trained model was **saved using Pickle and deployed as a web application**.

---

## 🎯 Objective
- Predict heart disease risk
- Compare multiple ML classification models
- Select the best-performing model using ROC–AUC
- Deploy the model with a web interface

---

## 🗂️ Dataset Processing

### 🔹 Data Preparation
- Dataset split into:
  - **Independent variables (X)**
  - **Dependent variable (y)**
- Used `train_test_split` to create:

- Checked for **null values**
- ✅ No null values found
- Dataset is **cleaned**
- **Outliers detected and handled**
- **Unnecessary columns removed** using feature selection
- Dataset **balanced** to handle class imbalance

---

## 🔄 Project Workflow
Load Dataset
↓
Split X and y
↓
Train-Test Split
↓
Outlier Handling
↓
Feature Selection
↓
Data Balancing
↓
Model Training
↓
Model Evaluation
↓
Best Model Selection
↓
Pickle Serialization
↓
Web Deployment
---

## ⚙️ Machine Learning Models Used

The following models were trained and evaluated:

- K-Nearest Neighbors (KNN)
- Naive Bayes
- Logistic Regression
- Decision Tree
- Random Forest
- AdaBoost Classifier
- Gradient Boosting
- Xtreme Gradient Boosting (XGBoost)

---

## 📊 Model Evaluation Metrics

Each model was evaluated using:
- ✔ Accuracy
- ✔ Classification Report
- ✔ Confusion Matrix
- ✔ ROC Curve
- ✔ AUC Score

---

## 📈 ROC–AUC Curve Analysis

ROC curves were plotted for all models to compare performance.


---

## 🏆 Best Model Selection

After comparing all evaluation metrics:

### 🥇 **Final Model: AdaBoost Classifier**

**Reasons:**
- Highest AUC score
- Better generalization
- Balanced precision and recall
- Strong performance on unseen data

---

## 💾 Model Saving (Pickle)

The following were saved using Pickle:
- Trained AdaBoost model
- Scaler
- Selected features


---

---

## 🌐 Web Application Deployment

- Created a web interface
- Users input medical details
- Model predicts heart disease detecetd or not
- Prediction displayed on the webpage

---

## 📦 requirements.txt

A `requirements.txt` file is included containing **all required libraries** to run the project.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Flask
- Pickle
- HTML / CSS

---



## 🚀 Conclusion
This project demonstrates a **complete machine learning workflow**, from data preprocessing to deployment.  
Using ROC–AUC analysis, **AdaBoost Classifier** was selected as the best model for heart disease risk prediction.

---


- Selected features

