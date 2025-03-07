import pandas as pd
import joblib

# Load model
model = joblib.load("../outputs/regression_model.pkl")

# Input new data
new_hours = [[9.25], [5.0], [2.0]]  # Example inputs
predictions = model.predict(new_hours)

# Save predictions
output_df = pd.DataFrame({"Hours": [x[0] for x in new_hours], "Predicted Scores": predictions})
output_df.to_csv("../outputs/predictions.csv", index=False)
print("Predictions saved.")
