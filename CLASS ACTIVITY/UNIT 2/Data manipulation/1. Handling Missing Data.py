import pandas as pd
import numpy as np

# Sample data with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 30, 22],
    'Salary': [50000, 60000, np.nan, 45000]
}

df = pd.DataFrame(data)

# Check missing values
print("Missing count:")
print(df.isnull().sum())

# Fill missing Age with median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Drop rows with missing Salary
df = df.dropna(subset=['Salary'])

print("\nCleaned DataFrame:")
print(df)
