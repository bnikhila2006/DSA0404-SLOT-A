import pandas as pd

data = {
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 75000, 90000, 110000],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'HR']
}

df = pd.DataFrame(data)

print("--- Numeric Summary ---")
print(df.describe())

print("\n--- Categorical Summary ---")
print(df.describe(include='str'))
