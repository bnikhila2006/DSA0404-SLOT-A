import pandas as pd
import numpy as np

raw_data = {
    "Employee_Name": [" Alice ", "Bob", "Charlie", "Diana", "Evan"],
    "Department": ["HR", "Engineering", "HR", "Engineering", "Marketing"],
    "Salary": [50000, 85000, np.nan, 92000, 60000],
    "Join_Date": [
        "2022-01-15",
        "2021-06-20",
        "2023-03-11",
        "2020-11-01",
        "2024-02-28"
    ]
}

df = pd.DataFrame(raw_data)

# Data Preprocessing
df["Employee_Name"] = df["Employee_Name"].str.strip()

median_salary = df["Salary"].median()
df["Salary"] = df["Salary"].fillna(median_salary)

df["Join_Date"] = pd.to_datetime(df["Join_Date"])

df["Years_of_Service"] = 2026 - df["Join_Date"].dt.year

print(df)
