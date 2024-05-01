# def sub(num1: int, num2: int) -> int:
#     """subtract two numbers"""
#     num3 = num2 - num1

#     return num3


# num1, num2 = 10, 100
# ans = sub(num1, num2)
# print(sub.__doc__)
# print(f"the subraction of {num1} and {num2} is {ans}.")

# def evenOdd(x):
#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("Odd")


# evenOdd(100)
# evenOdd(33)

x = 2
y = 3


def swap(x, y):
    temp = x
    x = y
    y = temp

    return x, y


x, y = swap(x, y)
print("new x: ", x)
print("new y: ", y)
