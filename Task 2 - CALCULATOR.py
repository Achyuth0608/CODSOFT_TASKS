print ("*****CALCUALTOR*****")
Number1 = float(input("Enter the first number ?\n"))
Number2 = float(input("Enter the second number ?\n"))
Operator = input("Enter the operation (+,-,*,/) :\n")

if Operator == '+':
    result = Number1 + Number2
elif Operator == '-':
    result = Number1 - Number2
elif Operator == '*':
    result = Number1 * Number2
elif Operator == '/':
    result = Number1 / Number2
else :
    print("OPERTOR ERROR")

print("RESULT = ", result)
