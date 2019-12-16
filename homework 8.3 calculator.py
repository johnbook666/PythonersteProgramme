print('--- calculator ---')
number1 = float(input('enter number 1: '))
number2 = float(input('enter number 2: '))
operation = input('enter operation: + - / *: ')
if operation == "+":
    result = number1 + number2
    print ('number 1 + number 2: ' + str(result))
elif operation == "-":
    result = number1 - number2
    print ('number 1 - number 2: ' + str(result))
elif operation == "/":
    result = number1 / number2
    print('number 1 / number 2: ' + str(result))
elif operation == "*":
    result = number1 * number2
    print('number 1 * number 2: ' + str(result))
else:
    print('wrong operation. try again :-)')