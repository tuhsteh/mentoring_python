
result = 0

calculation = input("What expression do you want to evaluate [e.g. 2 + 3]?  ")

pieces = calculation.split(" ")

for i in pieces:
    print("%s = %s" % (i, pieces[i]) )
    
num1 = float(pieces[0])
num2 = float(pieces[2])
oper = pieces[1]

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
