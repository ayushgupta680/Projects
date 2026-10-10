import pandas as pd
import numpy as np

df = pd.read_csv("sales.csv")
print(df)
print()

# Sales calculate

df["Sales"] = df["Quantity"] * df["Price"]
print("Total Sales:", np.sum(df["Sales"]))

# Best Selling Product

product = df.groupby("Product")["Quantity"].sum()
print("Best Selling Product:", product.idxmax())

# Monthly Sales

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month
monthly = df.groupby("Month")["Sales"].sum()
print("Monthly Sales:")
print(monthly)

# 4. Region-wise Sales

region = df.groupby("Region")["Sales"].sum()
print("Region Wise Sales:")
print(region)

#Average Order Value

print("Average order value:",np.mean(df["Sales"]))