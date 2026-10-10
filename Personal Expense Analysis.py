import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("expense.csv")

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

# Total expenses
total = np.sum(df["Amount"])
print("Total Expenses:", total)

# Monthly expenses
df["Month"] = df["Date"].dt.month
monthly = df.groupby("Month")["Amount"].sum()
print("\nMonthly Expenses:")
print(monthly)

# Most expensive category
category = df.groupby("Category")["Amount"].sum()
print("\nCategory-wise Expenses:")
print(category)

print("\nMost Expensive Category:", category.idxmax())

# Average daily spending
daily = df.groupby("Date")["Amount"].sum()
average_daily = np.mean(daily)
print("\nAverage Daily Spending:", round(average_daily, 2))

# Payment method usage
payment = df["Payment_Method"].value_counts()
print("\nPayment Method Usage:")
print(payment)

# Sort categories
print("\nSorted Expenses:")
print(category.sort_values(ascending=False))

plt.bar(category.index, category.values)
plt.xlabel("Category")
plt.ylabel("Amount")
plt.title("Category-wise Expenses")
plt.xticks(rotation=45)
plt.show()

plt.plot(monthly.index, monthly.values, marker="o")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.title("Monthly Expenses")
plt.show()

plt.plot(monthly.index, monthly.values, marker="o")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.title("Monthly Expenses")
plt.show()

plt.pie(category.values, labels=category.index, autopct="%1.1f%%")
plt.title("Expense Percentage by Category")
plt.show()