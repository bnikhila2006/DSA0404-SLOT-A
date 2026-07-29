from scipy.stats import norm

# Calculate cumulative probability
probability = norm.cdf(85, loc=70, scale=10)

print("Probability:", probability)
