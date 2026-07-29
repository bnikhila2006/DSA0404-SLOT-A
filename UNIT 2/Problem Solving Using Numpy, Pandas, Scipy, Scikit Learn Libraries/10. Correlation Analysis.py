from scipy.stats import pearsonr
# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
# Calculate Pearson correlation
corr, p_value = pearsonr(x, y)
# Display results
print("Correlation:", corr)
print("P-Value:", p_value)
