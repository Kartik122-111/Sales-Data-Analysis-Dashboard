import pandas as pd
import statistics
import numpy as np

# Load Dataset
df = pd.read_csv("sales_data.csv")

print("========== Sales Dataset ==========\n")
print(df)

sales = df["Sales"]

# Mean
print("\n========== Mean ==========")
print("Mean:", sales.mean())

# Median
print("\n========== Median ==========")
print("Median:", sales.median())

# Mode
print("\n========== Mode ==========")
print("Mode:", statistics.mode(sales))

# Maximum
print("\n========== Maximum ==========")
print(sales.max())

# Minimum
print("\n========== Minimum ==========")
print(sales.min())

# Range
print("\n========== Range ==========")
print(sales.max() - sales.min())

# Variance
print("\n========== Variance ==========")
print(np.var(sales))

# Standard Deviation
print("\n========== Standard Deviation ==========")
print(np.std(sales))

# Percentiles
print("\n========== Percentiles ==========")
print("25th Percentile:", np.percentile(sales, 25))
print("50th Percentile:", np.percentile(sales, 50))
print("75th Percentile:", np.percentile(sales, 75))

# Summary
print("\n========== Statistical Summary ==========")
print(df.describe())