import pandas as pd

data = {
    'Employee': ['Amy', 'John', 'Raj', 'Kevin', 'Sora'],
    'Department': ['HR', 'IT', 'IT', 'Sales', 'IT'],
    'Experience': [3, 7, 1, 5, 6]
}

df = pd.DataFrame(data)

# Filter employees in IT with experience > 5
filtered_df = df[(df['Department'] == 'IT') & (df['Experience'] > 5)]

print(filtered_df)
