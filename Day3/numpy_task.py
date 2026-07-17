# Import NumPy Library
import numpy as np


# Creating NumPy Array
numbers = np.array([12, 25, 36, 48, 55, 67, 78, 90])


# Display Array
print("Array:")
print(numbers)


# Array Properties
print("\nArray Dimension:")
print(numbers.ndim)

print("\nArray Size:")
print(numbers.size)


# Mathematical Operations

print("\nTotal Sum:")
print(np.sum(numbers))


print("\nAverage:")
print(np.mean(numbers))


print("\nMaximum Value:")
print(np.max(numbers))


print("\nMinimum Value:")
print(np.min(numbers))


# Sorting Array

print("\nSorted Array:")
print(np.sort(numbers))


# Basic Calculation

print("\nAddition with 10:")
print(numbers + 10)


print("\nMultiplication by 2:")
print(numbers * 2)