import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("employee_data.csv")

print("========== Employee Dataset ==========\n")
print(df)

# Dataset Information
print("\n========== Dataset Information ==========")
print(df.info())

# Statistical Summary
print("\n========== Statistical Summary ==========")
print(df.describe())

# Missing Values
print("\n========== Missing Values ==========")
print(df.isnull().sum())

# Duplicate Rows
print("\n========== Duplicate Rows ==========")
print(df.duplicated().sum())

# Average Salary
print("\nAverage Salary:", df["Salary"].mean())

# Maximum Salary
print("Maximum Salary:", df["Salary"].max())

# Minimum Salary
print("Minimum Salary:", df["Salary"].min())

# Employees with Salary > 45000
print("\n========== Employees with Salary > 45000 ==========")
print(df[df["Salary"] > 45000])

# Department Wise Average Salary
print("\n========== Department Wise Average Salary ==========")
print(df.groupby("Department")["Salary"].mean())

# Correlation
print("\n========== Correlation ==========")
print(df[["Age", "Salary", "Experience"]].corr())

# Bar Chart
plt.figure(figsize=(8,5))
df.groupby("Department")["Salary"].mean().plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.show()

# Line Chart
plt.figure(figsize=(8,5))
plt.plot(df["ID"], df["Salary"], marker="o")
plt.title("Salary Trend")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.grid(True)
plt.tight_layout()
plt.show()

print("\nEDA Completed Successfully!")