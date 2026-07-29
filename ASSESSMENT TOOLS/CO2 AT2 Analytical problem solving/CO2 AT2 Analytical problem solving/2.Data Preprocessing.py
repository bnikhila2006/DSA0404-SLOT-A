
# Remove extra spaces from employee names
df["Employee_Name"] = df["Employee_Name"].str.strip()

# Replace missing salary with the median salary
median_salary = df["Salary"].median()
df["Salary"] = df["Salary"].fillna(median_salary)

# Convert Join_Date to datetime format
df["Join_Date"] = pd.to_datetime(df["Join_Date"])

# Create a new column: Years of Service
df["Years_of_Service"] = 2026 - df["Join_Date"].dt.year

print("--- Preprocessed Data ---")
print(df)
