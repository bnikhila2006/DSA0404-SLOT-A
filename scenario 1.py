import numpy as np
# House data: Bedrooms, Sqft, Sale Price
house_data = np.array([
    [3, 1400, 7500000],
    [5, 2200, 12500000],
    [4, 1800, 9800000],
    [6, 3000, 18500000],
    [2, 1100, 5200000]
])
# Select houses with more than 4 bedrooms
filtered_houses = house_data[house_data[:, 0] > 4]
# Calculate average sale price
average_price = np.mean(filtered_houses[:, 2])
# Display results
print("Houses with more than 4 bedrooms:")
print(filtered_houses)
print("\nAverage Sale Price:", average_price)
