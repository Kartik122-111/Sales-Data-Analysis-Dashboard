import pandas as pd

# Read CSV File
df = pd.read_csv("sample_data.csv")

# Display Dataset
print("Employee Data")
print(df)

# Dataset Information
print("\nDataset Information")
print(df.info())

# First Five Rows
print("\nFirst Five Rows")
print(df.head())

# Last Five Rows
print("\nLast Five Rows")
print(df.tail())

# Statistical Summary
print("\nStatistical Summary")
print(df.describe())

# Department Column
print("\nDepartments")
print(df["Department"])

# Salary Column
print("\nSalary")
print(df["Salary"])

# Employees with Salary > 45000
print("\nEmployees with Salary Greater Than 45000")
print(df[df["Salary"] > 45000])

# Average Salary
print("\nAverage Salary")
print(df["Salary"].mean())

# Maximum Salary
print("\nMaximum Salary")
print(df["Salary"].max())

# Minimum Salary
print("\nMinimum Salary")
print(df["Salary"].min())

# Sort by Salary
print("\nSorted by Salary")
print(df.sort_values(by="Salary"))

# Save New CSV
df.to_csv("employee_output.csv", index=False)

print("\nemployee_output.csv created successfully!")