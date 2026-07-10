import numpy as np
brand = {
    "Maruti": 1,
    "Hyundai": 2,
    "Tata": 3,
    "Honda": 4,
    "Toyota": 5
}
X = np.array([
    [1, 25000, 1200],
    [2, 60000, 1500],
    [3, 40000, 1300],
    [4, 90000, 1800],
    [5, 15000, 1000]
], dtype=float)
y = np.array([650000, 420000, 520000, 300000, 720000], dtype=float)
ones = np.ones((X.shape[0], 1))
X = np.hstack((ones, X))
theta = np.linalg.inv(X.T @ X) @ X.T @ y
car_brand = input("Enter Car Brand (Maruti/Hyundai/Tata/Honda/Toyota): ")
kms = float(input("Enter Kilometers Driven: "))
engine = float(input("Enter Engine CC: "))
brand_code = brand[car_brand]
new_car = np.array([1, brand_code, kms, engine])
price = new_car @ theta
print("Estimated Resale Price = ₹", round(price, 2))
