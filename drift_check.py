import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# Load reference (training) data
reference_data = pd.read_csv("reference_data.csv")

# Load daily (current/production) data
current_data = pd.read_csv("daily_data.csv")

# Create drift report
report = Report(metrics=[
    DataDriftPreset()
])

report.run(
    reference_data=reference_data,
    current_data=current_data
)

# Save QA report
report.save_html("data_drift_report.html")

print("✅ Data drift report generated successfully")
