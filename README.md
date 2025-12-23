#  Heart Disease  Prediction using Machine Learning

## 📌 Project Overview
This project predicts the **risk of heart disease** using **Machine Learning classification algorithms**.  
The complete implementation is done using **classes, objects, and functions**, following a modular and structured approach.  
After comparing multiple models, **AdaBoost Classifier** was finalized as the best model and deployed as a **web application**.

---

## 🎯 Objective
To build an intelligent system that predicts whether a person has **heart disease or not** based on important medical features provided by the patient.

---

## 🧹 Data Preprocessing

### ✔ Data Splitting
- Independent variables → **X**
- Dependent variable → **y**
- Data split using **train_test_split()**

---

### ✔ Null Value Check
- Checked for missing values
- ✅ No null values found
- Dataset is **clean**

---

### ✔ Outlier Detection & Handling
- Outliers were identified
- Proper techniques applied to handle them

---

### ✔ Feature Selection
- Removed unnecessary and less important columns
- Improved model performance and efficiency

---

### ✔ Data Balancing
- Dataset was balanced to handle class imbalance
- Ensured fair learning for both classes

---

## 🤖 Machine Learning Models Used

| Model | Test Accuracy (%) |
|------|------------------|
| KNN | 80 |
| Naive Bayes | 80 |
| Logistic Regression | 84 |
| Decision Tree | 80 |
| Random Forest | 82 |
| **AdaBoost Classifier** | **90 ✅** |
| Gradient Boosting | 84 |
| Xtreme Gradient Boosting | 57 |

---

## 📊 Model Evaluation Metrics
For each model, the following were evaluated:
- ✔ Test Accuracy
- ✔ Classification Report
- ✔ Confusion Matrix
- ✔ ROC Curve
- ✔ AUC-ROC Score

Based on ROC and AUC-ROC curves, **AdaBoost Classifier** performed the best.

---

## 🏆 Best Model
**AdaBoost Classifier**
- Highest accuracy: **90%**
- Best ROC-AUC curve
- Good generalization performance

---

## 💾 Model Saving
- Final trained model saved using **Pickle**
- Enables reuse without retraining



## 🗂️ Dataset Description

### 🔹 Input Features (User Inputs)
The patient enters the following details:

| Feature | Description |
|------|------------|
| age | Age of the patient |
| sex | Gender (0 = Female, 1 = Male) |
| cp | Chest pain type |
| thalach | Maximum heart rate achieved |
| oldpeak | ST depression |
| slope | Slope of peak exercise ST segment |
| thal | Thalassemia |

---

### 🔹 Output
- **0** → No Heart Disease Detected  
- **1** → Heart Disease Detected  


---

- Patients enter medical details
- The model predicts heart disease risk instantly


---

## ✅ Conclusion
This project successfully builds and deploys a **heart disease risk prediction system** using machine learning.  
Among all evaluated models, **AdaBoost Classifier** achieved the best performance and was implemented in a real-time web application.

---

