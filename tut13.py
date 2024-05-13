# simple for loop
# fruits = ["apple", "banana", "orange"]

# for fruit in fruits:
#     print(fruit)

# converting strings into individual letter
# word = "Python"
# for letter in word:
#     print(letter)

# Using for loop with range
# for i in range(5):
#     print(i)

# using for loop on dictionary
# person = {"name": "Sohail", "age": "26", "city": "Ajman"}
# for key, value in person.items():
#     print(f"{key}: {value}")


# nested loops
# for i in range(3):
#     for j in range(5):
#         print(f"({i}, {j})")

# skipping elements with continue:
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num % 2 == 0:
#         print(num)
#         continue

# Breaking the loop with break:
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num == 4:
#         break
#     print(num)


# looping through multiple sequences simultaneously:
# name = ["sohail", "rashed"]
# age = [26, 60]

# for name, age in zip(name, age):
#     print(f"{name} is {age} years old")

# Looping using enumerate to get index and value
# colors = ["red", "green", "blue"]
# for index, color in enumerate(colors):
#     print(f"Color {index + 1}: {color}")

# iterating over a list in reverse:
# numbers = [1, 2, 3, 4, 5]
# for num in reversed(numbers):
#     print(num)

# calculate the average temperature for each day of week and print result:

# Temperatures = {(28, 38), (23, 35), (24, 32), (21, 30),
#                 (24, 30), (25, 38), (20, 30)}


# for index, temprature in enumerate(Temperatures, start=1):
#     aveg = (temprature[0] + temprature[1])/2
#     print(f"Day {index}: Average temperature is {aveg:.2f}° C ")

# using continue statement in nested loop
# for i in range(2, 4):
#     for j in range(1, 11):
#         if i == j:
#             continue
#         print(i, "*", j, "=", i * j)

#     print()

# using list comprehension to make nested loop statement in single line

# list1 = [[j for j in range(5)]for i in range(2)]

# print(list1)
