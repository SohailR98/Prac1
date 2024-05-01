# tutorial to use tuple and list

T = (3, 4, 5, 3, 2)
print("Tuple before adding new element")
print(T)
L = list(T)
L.append(int(input("Enter the new element: ")))
T = tuple(L)
print("Tuple after adding new element")
print(T)
