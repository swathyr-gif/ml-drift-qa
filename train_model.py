import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset (this is your TRAINING DATA)
data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Save reference data for QA comparison
X.to_csv("reference_data.csv", index=False)

# Train baseline model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Save trained model
joblib.dump(model, "baseline_model.pkl")

print("✅ Baseline model trained")
print("✅ Reference data saved")
