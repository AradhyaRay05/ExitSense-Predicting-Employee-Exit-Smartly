# ExitSense – Predicting Employee Exit Smartly

## 🚀 Project Goal

**ExitSense** is a smart machine learning-powered web application designed to predict whether an employee is likely to exit a company based on key workplace features. It empowers HR teams with data-driven insights to proactively address attrition and improve retention strategies.

---

## 📌 Project Overview

Employee turnover is a major challenge for organizations, especially when exits are unexpected. ExitSense uses historical HR data and a trained machine learning model to identify exit risks based on factors like satisfaction level, evaluation scores, number of projects, and more.

With an intuitive Streamlit interface, HR professionals or analysts can input employee data and receive real-time predictions on whether an employee is likely to leave or stay.

---

## 🔁 Project Workflow

### 1. **Data Preprocessing**
- Loaded and explored the HR dataset
- Checked for missing/null values and outliers
- Converted categorical features like `department` and `salary` using **one-hot encoding**
- Combined similar roles (e.g., *support* and *IT* merged into *technical*) to simplify modeling
- Applied **feature scaling** using `StandardScaler` to normalize input data for the model

### 2. **Model Building**
- Implemented and evaluated both **Logistic Regression** and **Random Forest Classifier**
- After comparing model performance, **Random Forest** was selected as the final model due to its superior accuracy and robustness
- Random Forest achieved an accuracy of **98%**, outperforming Logistic Regression

### 3. **Evaluation Metrics**
- **Accuracy:** 98% (on test data)
- Other metrics considered: Precision, Recall, F1-Score
- Evaluated using confusion matrix and classification report

### 4. **Deployment**
- Final model and scaler were saved using `joblib`
- Built an interactive web app with **Streamlit** for live predictions
- Input features are collected using sliders and dropdowns

---

## 🧰 Tech Stack

- **Frontend & Interface:** Streamlit
- **Programming Language:** Python 3.11
- **Modeling & ML:** Scikit-learn, NumPy, Pandas, Joblib
- **Visualization:** Matplotlib, Seaborn, Plotly
- **Environment:** Jupyter Notebook

---

## 📁 Project Structure

```bash
ExitSense/
├── Dataset/
│   └── dataset.csv                  # HR dataset used for training
├── Employee_Turnover_Prediction.ipynb  # Notebook for EDA and model training
├── app.py                           # Streamlit app interface
├── model.pkl                        # Trained Random Forest model
├── scaler.pkl                       # StandardScaler for input features
├── requirements.txt                # Project dependencies
└── README.md                       # Project documentation
```


## 🌟 Features

- Clean and interactive UI for HR personnel
- Real-time prediction of employee exit
- Scalable and easy to customize with new features
- Designed to support proactive decision-making in HR

---

## 🔮 Future Enhancements

- Add login-based dashboards for different HR roles
- Include more advanced models like XGBoost or ensemble stacks
- Visual analytics dashboard using Plotly or Dash
- Real-time integration with company databases or APIs
- Alert system or retention suggestion engine
- Deploy to cloud using Docker, Streamlit Sharing, or AWS

---

## 📬 Contact

<p>
  <a href="mailto:aradhyaray99@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="https://www.linkedin.com/in/rayaradhya"><img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://github.com/AradhyaRay05"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>

---

Thanks for visiting ! Feel free to explore my other repositories and connect with me. 🚀 
