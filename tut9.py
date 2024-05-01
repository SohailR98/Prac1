L = "Resistance"
for i in L:
    print(i)

for i in range(0, 10, 4):
    print(i)

for i in range(0, 10, 5):
    for j in range(0, 10, 2):
        print(i, j)


first = ["Sohail"]
last = ["Rashed", "Mohammed", "Khan"]

for first, last in zip(first, last):
    print(first, " ", last)

for letters in "geeksforgeeks":
    if letters == 'e' or letters == 's':
        print('Break Letter :', letters)
        break

    print('Normal Letter :', letters)
