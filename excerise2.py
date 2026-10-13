operator = input(f"Enter a operator (+,-,*,/): ")
num1 = float(input('Enter the first number:'))
num2 = float(input("Enter the second number:"))

if operator == '+':
    print(f'{num1} + {num2} = {num1 + num2}')
elif operator == '-':
    print(f'{num1} - {num2} = {num1 - num2}')
elif operator == '*':
    print(f'{num1} * {num2} = {num1 *num2}')
elif operator == '/':
    if num2 != 0:
        print(f'{num1} / {num2} = {num1 / num2}')
    else:
        print('error numbers can not be divide by zero')
else:
    print('Pls input a valid operator from the list given')











