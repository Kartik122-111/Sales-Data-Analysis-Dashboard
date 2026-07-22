import pandas as pd

# Load Dataset
df = pd.read_csv("dirty_employee_data.csv")

print("========== Original Dataset ==========\n")
print(df)

# Missing Values
print("\n========== Missing Values ==========")
print(df.isnull().sum())

# Fill Missing Values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("\n========== Dataset After Filling Missing Values ==========\n")
print(df)

# Duplicate Rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove Duplicates
df = df.drop_duplicates()

print("\n========== Dataset After Removing Duplicates ==========\n")
print(df)

# Rename Columns
df = df.rename(columns={
    "Salary": "Monthly_Salary",
    "Experience": "Years_of_Experience"
})

print("\n========== Renamed Columns ==========\n")
print(df.head())

# Create New Column
df["Bonus"] = df["Monthly_Salary"] * 0.10

print("\n========== Dataset with Bonus Column ==========\n")
print(df)

# Save Cleaned Dataset
df.to_csv("cleaned_employee_data.csv", index=False)

print("\nCleaned dataset saved successfully as cleaned_employee_data.csv")