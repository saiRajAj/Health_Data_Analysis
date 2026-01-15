import pandas as pd

df = pd.read_csv("cleaned_data.csv")

print("\nStatistical Summary:")
print(df.describe())

print("\nDisease Distribution:")
print(df['Disease'].value_counts())
