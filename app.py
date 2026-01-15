import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Health Risk Prediction", layout="centered")
st.title("🏥 Health Risk Prediction System")

# Load data
df = pd.read_csv("dataset/health_data.csv")

# Encode categorical features
le = LabelEncoder()
for col in ['Gender', 'Smoking', 'PhysicalActivity']:
    df[col] = le.fit_transform(df[col])

X = df.drop("Disease", axis=1)
y = df["Disease"]

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

st.header("Enter Patient Details")

age = st.slider("Age", 18, 80)
gender = st.selectbox("Gender", ["Male", "Female"])
bmi = st.slider("BMI", 15.0, 40.0)
bp = st.slider("Blood Pressure", 80, 180)
glucose = st.slider("Glucose Level", 70, 250)
chol = st.slider("Cholesterol Level", 150, 300)
smoking = st.selectbox("Smoking", ["Yes", "No"])
activity = st.selectbox("Physical Activity", ["Low", "Medium", "High"])

input_df = pd.DataFrame([[
    age,
    1 if gender == "Male" else 0,
    bmi,
    bp,
    glucose,
    chol,
    1 if smoking == "Yes" else 0,
    {"Low": 0, "Medium": 1, "High": 2}[activity]
]], columnzs=X.columns)

if st.button("Predict Disease Risk"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("⚠️ High Risk of Disease")
    else:
        st.success("✅ Low Risk of Disease")
