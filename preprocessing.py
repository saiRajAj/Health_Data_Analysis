import pandas as pd

df = pd.read_csv("dataset/health_data.csv")

print("Original Data:")
print(df)

# Encode categorical columns
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
df['Smoking'] = df['Smoking'].map({'Yes': 1, 'No': 0})
df['PhysicalActivity'] = df['PhysicalActivity'].map({
    'Low': 0,
    'Medium': 1,
    'High': 2
})

print("\nProcessed Data:")
print(df)

df.to_csv("cleaned_data.csv", index=False)
