import pandas as pd
import matplotlib.pyplot as plt

# Create sample dataset
data = {
    'Name': ['Arun', 'Bala', 'Chitra', 'Divya', 'Ezhil', 'Fathima'],
    'Department': ['CSE', 'ECE', 'CSE', 'ECE', 'CSE', 'ECE'],
    'Marks': [85, 78, 92, 88, 75, 95]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)
print("\nSorted by Marks:")
sorted_df = df.sort_values(by='Marks', ascending=False)
print(sorted_df)
