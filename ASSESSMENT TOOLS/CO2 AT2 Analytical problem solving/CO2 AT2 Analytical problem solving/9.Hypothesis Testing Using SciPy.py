from scipy import stats

# Sample data
data = [22, 25, 19, 24, 28, 30]

# One-sample t-test
t_stat, p_value = stats.ttest_1samp(data, 25)

# Display results
print("T-Statistic:", t_stat)
print("P-Value:", p_value)
