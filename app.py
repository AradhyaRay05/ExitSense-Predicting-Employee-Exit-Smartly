import streamlit as st
import joblib
import numpy as np

# Load model and scaler
@st.cache_resource
def load_model():
    model = joblib.load(r"D:\Education\Coding\Machine Learning\Machine Learning Projects\New folder\Employee Turnover Prediction copy\model.pkl")
    scaler = joblib.load(r"D:\Education\Coding\Machine Learning\Machine Learning Projects\New folder\Employee Turnover Prediction copy\scaler.pkl")
    return model, scaler

model, scaler = load_model()

st.title("Employee Turnover Prediction")

# Example input fields (customize according to your model's features)
satisfaction_level = st.slider("Satisfaction Level", 0.0, 1.0, 0.5)
last_evaluation = st.slider("Last Evaluation", 0.0, 1.0, 0.5)
number_project = st.number_input("Number of Projects", 1, 10, 3)
average_monthly_hours = st.slider("Average Monthly Hours", 50, 400, 160)
time_spend_company = st.number_input("Time Spent at Company (years)", 1, 10, 3)
work_accident = st.selectbox("Work Accident", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
promotion_last_5years = st.selectbox("Promotion in Last 5 Years", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
department = st.selectbox("Department", ["sales", "technical", "support", "IT", "hr", "accounting", "marketing", "product_mng", "management", "RandD"])
salary = st.selectbox("Salary", ["low", "medium", "high"])

# One-hot encode department and salary
departments = ["sales", "technical", "hr", "accounting", "marketing", "product_mng", "management", "RandD"]
salaries = ['high', 'low', 'medium']

# Merge support and IT into technical for input
if department in ["support", "IT"]:
    department = "technical"

department_ohe = [1 if department == d else 0 for d in departments]
salary_ohe = [1 if salary == s else 0 for s in salaries]

input_data = np.array([[
    satisfaction_level,
    last_evaluation,
    number_project,
    average_monthly_hours,
    time_spend_company,
    work_accident,
    promotion_last_5years,
    *department_ohe,
    *salary_ohe
]])

# Scale input
input_scaled = scaler.transform(input_data)

if st.button("Predict"):
    prediction = model.predict(input_scaled)
    if prediction[0] == 1:
        st.error("This employee is likely to leave.")
    else:
        st.success("This employee is likely to stay.")