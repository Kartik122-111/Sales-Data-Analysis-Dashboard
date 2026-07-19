import pandas as pd
import matplotlib.pyplot as plt

# Read CSV File
df = pd.read_csv("sales_data.csv")

print("Sales Dataset")
print(df)

# -----------------------
# Line Chart
# -----------------------
plt.figure(figsize=(8,5))
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------
# Bar Chart
# -----------------------
plt.figure(figsize=(8,5))
plt.bar(df["Month"], df["Sales"])
plt.title("Monthly Sales Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------
# Pie Chart
# -----------------------
plt.figure(figsize=(7,7))
plt.pie(
    df["Sales"],
    labels=df["Month"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Sales Distribution")
plt.show()

# -----------------------
# Histogram
# -----------------------
plt.figure(figsize=(7,5))
plt.hist(df["Sales"], bins=5)
plt.title("Sales Histogram")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# -----------------------
# Scatter Plot
# -----------------------
plt.figure(figsize=(8,5))
plt.scatter(df["Month"], df["Sales"])
plt.title("Sales Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\nAll charts generated successfully!")