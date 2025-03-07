import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../outputs/cleaned_data.csv")

# Summary statistics
print(df.describe())

# Visualizations
sns.pairplot(df)
plt.savefig("../outputs/pairplot.png")

plt.figure(figsize=(6, 4))
sns.scatterplot(x=df["Hours"], y=df["Scores"])
plt.xlabel("Hours Studied")
plt.ylabel("Scores")
plt.savefig("../outputs/scatterplot.png")
print("Exploratory analysis completed.")
