parts = input("Enter two values : ").split()

integer_values = [int(part) for part in parts]

print("Number of boys: ", integer_values[0])
print("Number of girls:", integer_values[1])
print("Total number of students:", integer_values[0] + integer_values[1])

x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)
