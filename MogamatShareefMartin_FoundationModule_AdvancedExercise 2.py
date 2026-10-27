# -------------------------------------------
# Advanced Python Challenge: Exercise 02 Operators and Conditionals
# -------------------------------------------

# Overview:
# This exercise challenges your understanding of Python operators, conditionals, and input handling.
# Complete each section with the required logic, using good variable names and adding comments where necessary.

# -------------------------------------------
# Question 1: Multi-Step Arithmetic Operations
# -------------------------------------------

# Task:
# Use compound arithmetic operators to modify values of a, b, and c.
# Then calculate the square root of the sum of their squares.
# Tip: Use the math module.

import math

# Start with some base values
a = 5
b = 10
c = 7

# TODO: Add 3 to a using +=
a += 3

# TODO: Multiply b by 2 using *=
b *= 2

# TODO: Modulo c by 4 using %=
c %= 4

# TODO: Calculate the square root of (a^2 + b^2 + c^2)
square = a**2 + b**2 + c**2
square_root = math.sqrt(square)
rounded_square = round(square_root, 2)

# TODO: Print the final result rounded to 2 decimal places
print(rounded_square)

# -------------------------------------------
# Question 2: Complex Conditional Evaluation
# -------------------------------------------

# Task:
# Ask the user to input three integers (x, y, z).
# Then evaluate and print whether:
# - x is even
# - y is positive
# - z is between 10 and 50
# Use logical operators to combine the conditions.

# Tip: Use and/or to join conditions.

# TODO: Input x, y, z
x = int(input("Input number for x: "))
y = int(input("Input number for y: "))
z = int(input("Input number for z: "))

# TODO: Create conditions:
is_even =  x % 2 == 0
is_positive = y > 0
is_in_range = 10 < z < 50

# TODO: Create final_condition = is_even and is_positive and is_in_range
final_condition = is_even and is_positive and is_in_range

# TODO: Print final_condition
print(final_condition)

# -------------------------------------------
# Question 3: Grading with Adjustments
# -------------------------------------------

# Task:
# Ask the user for their base score, then apply:
# - bonus points (+5)
# - late penalty (-10)
# Final score must not exceed 100 or drop below 0.
# Then assign a grade.

# Tip: Use min() and max() to constrain the score.

# TODO: Input score from user
user_score = int(input("Enter your score: "))

# TODO: Apply adjustments
bonus = 5
late = -10
final_score = user_score + bonus + late

# TODO: Clamp score between 0 and 100
min_score = 0
max_score = 100
clamped_score = max(min_score, min(final_score, max_score))

# TODO: Use if-elif-else to determine grade and print it
if clamped_score >= 90:
  print("A")

elif clamped_score >= 80:
  print("B")

elif clamped_score >= 70:
  print("C")

elif clamped_score >= 60:
  print("D")

else:
  print("F")

# -------------------------------------------
# Question 4: Advanced Calculator
# -------------------------------------------

  # Task:
  # Ask the user to input two numbers and an operation (+, -, *, /, %, **).
  # Handle division/modulus by zero with error checking.
  # Perform the operation and print the result.

  # Tip: Use try-except and elif branches for each operation.
try:

  # TODO: Input num1, num2
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))

  # TODO: Input operation
  operation = input("Enter operation (+, -, *, /, %, **): ")

  # TODO: Match operation using if-elif
  if operation == "+":
    result = num1 + num2

  elif operation == "-":
    result = num1 - num2

  elif operation == "*":
    result = num1 * num2

  elif operation == "**":
    result = num1 ** num2

  # TODO: Handle division/modulus by zero with try-except
  elif operation == "/":
    if num2 == 0:
      raise(ZeroDivisionError("Error! Division by 0 is impossibe!"))
    else:
      result = num1 / num2

  elif operation == "%":
      if num2 == 0:
        raise(ZeroDivisionError("Error! Modulus Division by 0 is impossibe!"))
      else:
        result = num1 % num2

  else:
    print("Error! Invalid operation selected!")
    result = None

  # TODO: Print result
  if result is not None:
    print(result)

except ValueError:
  print("Error! Please enter numerical values only!")

except ZeroDivisionError as e:
  print(e)