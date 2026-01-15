import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")

X = df.drop("Disease", axis=1)
y = df["Disease"]

# Train model
model = LogisticRegression()
model.fit(X, y)

print("\n--- Enter New Patient Details ---")

# Taking inputs from user
age = int(input("Enter Age: "))
gender = input("Enter Gender (Male/Female): ").strip().lower()
bmi = float(input("Enter BMI: "))
bp = int(input("Enter Blood Pressure: "))
glucose = int(input("Enter Glucose Level: "))
cholesterol = int(input("Enter Cholesterol Level: "))
smoking = input("Smoking (Yes/No): ").strip().lower()
activity = input("Physical Activity (Low/Medium/High): ").strip().lower()

# Encoding inputs
gender = 1 if gender == "male" else 0
smoking = 1 if smoking == "yes" else 0

if activity == "low":
    activity = 0
elif activity == "medium":
    activity = 1
else:
    activity = 2

# Create DataFrame
new_patient = pd.DataFrame({
    "Age": [age],
    "Gender": [gender],
    "BMI": [bmi],
    "BloodPressure": [bp],
    "Glucose": [glucose],
    "Cholesterol": [cholesterol],
    "Smoking": [smoking],
    "PhysicalActivity": [activity]
})

# Prediction
prediction = model.predict(new_patient)
probability = model.predict_proba(new_patient)[0][1]

print("\n--- Prediction Result ---")
print(f"Disease Probability: {probability:.2f}")

if prediction[0] == 1:
    print("⚠️ Disease Risk Detected")
else:
    print("✅ No Disease Risk")
