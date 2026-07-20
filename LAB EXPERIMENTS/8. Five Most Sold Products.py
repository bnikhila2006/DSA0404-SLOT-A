import pandas as pd

df = pd.read_csv("8.data_txt.txt")

top_5_products = df.groupby("Product_Name")["Price"].sum().nlargest(5)

print("Five most sold products:")
print(top_5_products)
