print('''Welcome to Calculator

Operations
1. (Addiction)
2. (Subtraction)
3. (Multiplication)
4. (Division)
5. (Power)
6. (Sqaure Root)
7. (Modulo)
8. (Floor Division)
q  (Close Program)''')

operation = input('Select an option: ')

if operation == '1':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
	print(number_1, "+", number_2, "=", number_1 + number_2)

elif operation == '2':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
	print(number_1, '-', number_2, '=', number_1 - number_2)

elif operation == '3':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
	print(number_1, 'x', number_2, '=', number_1 * number_2)

elif operation == '4':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
	print(number_1, '÷', number_2, '=', number_1 / number_2)

elif operation == '5':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
	print(number_1, '^', number_2, '=', number_1 ** number_2)

elif operation == '6':
        number = int(input('Enter your number: '))
	import math
	print('√', number, '=', math.sqrt(number))
        
elif operation == '7':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
	print(number_1, '%', number_2, '=', number_1 % number_2)
        
elif operation == '8':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
	print(number_1, '//', number_2, '=', number_1 // number_2)

elif operation == 'q':
	exit()

else:
        exit()

input('Press enter to quit')

Links:
# https://www.digitalocean.com/community/tutorials/how-to-make-a-simple-calculator-program-in-python-3
# https://www.programiz.com/python-programming/examples/calculator
# https://en.wikibooks.org/wiki/Python_Programming/Basic_Math
