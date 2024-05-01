# nested loop

# x = [1, 2]
# y = [4, 5]
# i = 0

# while i < len(x):
# j = 0
# while j < len(y):
# print(x[i], y[j])
#   j = j + 1
#  i = i + 1

# multiplication table

# for i in range(5, 7):
#   for j in range(10, 101, 10):
#   print(i, "*", j, "=", i*j)

# print()


list1 = ["I am", "You are"]
list2 = ["Healthy", "good", "Sad"]

list2_size = len(list2)

for item in list1:
    print("Start of loop")
    i = 0
    while (i < list2_size):
        print(item, list2[i])

        i = i + 1

    print("end of loop")
