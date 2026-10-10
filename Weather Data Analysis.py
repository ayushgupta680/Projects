import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv")
print(df)
print()

df["Date"] = pd.to_datetime(df["Date"])

#Average Temperature

avg_temp = np.mean(df["Temperature"])
print("Average Temperature:", round(avg_temp, 2))

#Hottest Day

hottest = df.loc[df["Temperature"].idxmax()]
print(hottest)
print()

#Coldest Day

coldest = df.loc[df["Temperature"].idxmin()]
print(coldest)
print()

#Total Rainfall

total_rainfall = np.sum(df["Rainfall"])
print("Total Rainfall:", total_rainfall)

#Average Humidity

avg_humidity = np.mean(df["Humidity"])
print("Average Humidity:", round(avg_humidity, 2))

#Charts

#Temperature over Time

plt.figure(figsize=(10,5))
plt.plot(df["Date"], df['Temperature'], marker = "o")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Temperature Over Time")
plt.xticks(rotation = 45)
plt.show()

#Rainfall Bar Chart

plt.figure(figsize=(10,5))
plt.bar(df["Date"], df["Rainfall"])
plt.xlabel("Date")
plt.ylabel("Rainfall")
plt.title("Rainfall")
plt.xticks(rotation = 45)
plt.show()

#Temperature vs Humidity

plt.figure(figsize=(8,5))
plt.bar(df["Temperature"], df["Humidity"])
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.title("Temperature vs Humidity")
plt.show()