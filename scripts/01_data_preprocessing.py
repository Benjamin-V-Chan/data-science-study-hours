import pandas as pd
import os

# Load dataset
df = pd.read_csv("../data/score.csv")

# Check for missing values
df.dropna(inplace=True)

# Ensure correct data types
df["Hours"] = df["Hours"].astype(float)
df["Scores"] = df["Scores"].astype(int)

# Save cleaned dataset
os.makedirs("../outputs/", exist_ok=True)
df.to_csv("../outputs/cleaned_data.csv", index=False)
print("Data preprocessing completed.")