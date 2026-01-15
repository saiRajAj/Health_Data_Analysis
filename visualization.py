import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cleaned_data.csv")

# Age distribution
plt.figure()
sns.histplot(df["Age"], kde=True)
plt.title("Age Distribution")
plt.show()

# BMI vs Disease
plt.figure()
sns.boxplot(x="Disease", y="BMI", data=df)
plt.title("BMI vs Disease")
plt.show()

# Correlation heatmap
plt.figure()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
