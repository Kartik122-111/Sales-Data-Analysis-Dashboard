import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Load Dataset
df = pd.read_csv("employee_data.csv")

print("========== Original Dataset ==========\n")
print(df)

# ------------------------------------
# Feature Engineering
# ------------------------------------

# Bonus = 10% Salary
df["Bonus"] = df["Salary"] * 0.10

# Total Income
df["Total_Income"] = df["Salary"] + df["Bonus"]

print("\n========== After Feature Engineering ==========\n")
print(df)

# ------------------------------------
# Label Encoding
# ------------------------------------

label = LabelEncoder()

df["Department_Label"] = label.fit_transform(df["Department"])

print("\n========== Label Encoding ==========\n")
print(df[["Department","Department_Label"]])

# ------------------------------------
# One Hot Encoding
# ------------------------------------

one_hot = pd.get_dummies(df["Department"], prefix="Dept")

df = pd.concat([df, one_hot], axis=1)

print("\n========== One Hot Encoding ==========\n")
print(df)

# ------------------------------------
# Feature Scaling
# ------------------------------------

scaler = MinMaxScaler()

df["Salary_Scaled"] = scaler.fit_transform(df[["Salary"]])

print("\n========== Min-Max Scaling ==========\n")
print(df[["Salary","Salary_Scaled"]])

# Save Dataset
df.to_csv("feature_engineered_data.csv", index=False)

print("\nFeature Engineered Dataset Saved Successfully!")