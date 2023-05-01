num1 = 0

while True:
    
    if num1 == 0 :
        num1 = int(input("Enter the first number"))

    operator = input("Enter any of the following *, -, +, /")
    num2 = int(input("Enter the second number"))
    if operator == "*":
        result = num1 * num2
        print("The result is = ", result)
        

    elif operator == "+":
         result = num1 + num2
         print("The result is = ", result)
         

    elif operator == "-":
         result = num1 - num2
         print("The result is = ", result)
         
    
    elif operator == "/":
         result = num1 / num2
         print("The result is = ", result)
         
    else :
         print("Invalid Operator")
         continue
    
    print("Result = ", result)

    choice = input("Do you want to start a new calculation? Y/N :")

    if choice.lower() == "y" :
         num1 = 0 

    else: 
         num1 = result
         continue 