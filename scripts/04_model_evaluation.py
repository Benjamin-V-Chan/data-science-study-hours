import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load model and test data
df = pd.read_csv("../outputs/cleaned_data.csv")
X = df[["Hours"]]
y = df["Scores"]
model = joblib.load("../outputs/regression_model.pkl")

# Predictions
y_pred = model.predict(X)

# Evaluation metrics
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

# Save results
with open("../outputs/evaluation_results.txt", "w") as f:
    f.write(f"MAE: {mae}\nMSE: {mse}\nR2 Score: {r2}\n")
print("Model evaluation completed.")