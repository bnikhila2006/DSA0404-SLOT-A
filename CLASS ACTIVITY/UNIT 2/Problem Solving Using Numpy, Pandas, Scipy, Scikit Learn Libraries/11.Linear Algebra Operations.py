from scipy import linalg
# Coefficient matrix
A = [[3, 2],
     [1, 2]]
# Constant values
B = [5, 5]
# Solve the linear equations
solution = linalg.solve(A, B)
# Display the solution
print(solution)
