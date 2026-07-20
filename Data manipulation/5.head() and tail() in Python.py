import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
    'Score': [85, 92, 78, 95, 88, 72, 91]
}

df = pd.DataFrame(data)

# First 5 rows
print(df.head())

# First 2 rows
print(df.head(2))

# Last 3 rows
print(df.tail(3))
