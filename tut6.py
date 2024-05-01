List = list()
Set = set()
l = int(input("Enter the size of list : "))
s = int(input("Enter the size of Set : "))
print("Enter the numbers of list :")
for i in range(0, l):
    List.append(int(input()))
print("Enter the numbers of Set : ")
for i in range(0, s):
    Set.add(int(input()))

print(List)
print(Set)
