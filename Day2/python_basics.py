# ==========================================
# Day 2 - Python Basics
# Codomax Data Science Internship
# Author: Kartik Thate
# ==========================================

print("========== VARIABLES ==========")
name = "Kartik"
age = 18
course = "Data Science"

print("Name:", name)
print("Age:", age)
print("Course:", course)

print("\n========== DATA TYPES ==========")
print(type(name))
print(type(age))

height = 5.8
student = True

print(type(height))
print(type(student))

print("\n========== OPERATORS ==========")
a = 20
b = 10

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Modulus =", a % b)

print("\n========== IF ELSE ==========")
marks = 75

if marks >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")

print("\n========== FOR LOOP ==========")
for i in range(1, 6):
    print(i)

print("\n========== WHILE LOOP ==========")
count = 1

while count <= 5:
    print(count)
    count += 1

print("\n========== FUNCTION ==========")

def greet(name):
    print("Welcome", name)

greet("Kartik")

print("\n========== MINI PROGRAM ==========")

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)

if num2 != 0:
    print("Division =", num1 / num2)
else:
    print("Division by zero is not allowed.")

print("\nDay 2 Completed Successfully!")