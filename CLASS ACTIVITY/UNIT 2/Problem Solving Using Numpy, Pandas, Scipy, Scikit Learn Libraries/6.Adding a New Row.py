import pandas as pd

# Create the original DataFrame
df = pd.DataFrame()

df['Name'] = ['John', 'Emma', 'Liam', 'Olivia']
df['Age'] = [20, 19, 21, 18]
df['Student'] = [True, True, False, True]

# Create a new row
new_row = pd.DataFrame([['Sophia', 22, False]],
                       columns=['Name', 'Age', 'Student'])

# Add the new row
df = pd.concat([df, new_row], ignore_index=True)

# Display the updated DataFrame
print(df)
