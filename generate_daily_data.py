import pandas as pd
import numpy as np

# Load reference data
reference = pd.read_csv("reference_data.csv")

# Simulate real-world data drift
daily_data = reference.copy()
daily_data += np.random.normal(0, 0.5, daily_data.shape)

# Save daily data
daily_data.to_csv("daily_data.csv", index=False)

print("✅ Daily production data generated")
