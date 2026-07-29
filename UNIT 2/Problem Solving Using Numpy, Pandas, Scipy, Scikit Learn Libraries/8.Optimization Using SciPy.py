from scipy.optimize import minimize
# Objective function
def objective(x):
    return x**2 + 4
# Find the minimum value
result = minimize(objective, x0=5)
# Display the optimal value of x
print(result.x)
