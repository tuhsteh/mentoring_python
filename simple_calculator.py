
result = 0

num1 = float(input ("Insert first number here,  "))
num2 = float(input ("Insert second number here,  "))
oper = input("Which operator do you want [+-/*]?  ")

if (oper == '+'):
    result = num1 + num2
elif (oper == '-'):
    result = num1 - num2
elif (oper == '*'):
    result = num1 * num2
elif (oper == '/'):
    result = num1 / num2
else:
    raise ValueError("Unsupported operator.")

print( "Result = %g" % result )
