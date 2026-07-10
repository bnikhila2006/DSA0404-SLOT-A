import numpy as np
# Training data
X = np.array([
    [1, 3, 120],
    [6, 15, 300],
    [0, 1, 80],
    [4, 10, 250],
    [2, 5, 160]
], dtype=float)
# Output (Spam)
y = np.array([[0], [1], [0], [1], [0]])
# Normalize features
X = X / X.max(axis=0)
weights = np.zeros((3, 1))
bias = 0
learning_rate = 0.1
epochs = 1000
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
for i in range(epochs):
    z = np.dot(X, weights) + bias
    y_pred = sigmoid(z)
    dw = (1 / len(X)) * np.dot(X.T, (y_pred - y))
    db = (1 / len(X)) * np.sum(y_pred - y)
    weights -= learning_rate * dw
    bias -= learning_rate * db
new_email = np.array([[5, 12, 280]], dtype=float)
new_email = new_email / np.array([6, 15, 300])
result = sigmoid(np.dot(new_email, weights) + bias)
if result >= 0.5:
    print("Prediction: Spam Email")
else:
    print("Prediction: Not Spam Email")
