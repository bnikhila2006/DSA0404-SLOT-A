import pandas as pd

df = pd.read_csv("data_txt.txt")

total_orders = df.groupby("Full Name")["Order Count"].sum()
avg_order_per_product = df.groupby("Items")["Order Total"].mean()

earliest_order = df["Order"].min()
latest_order = df["Order"].max()

print("Total number of orders made by each customer:")
print(total_orders)

print("\nAverage order quantity for each product:")
print(avg_order_per_product)

print("\nEarliest order date:", earliest_order)
print("Latest order date:", latest_order)
