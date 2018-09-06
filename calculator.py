print('Welcome to Calculator')
print('')
print('Operations')
print('')
print('add  (Addiction)')
print('sub  (Subtraction)')
print('mul  (Multiplication)')
print('div  (Division)')
print('pow  (Power)')
print('sq   (Sqaure Root)')
print('mod  (Modulo)')
print('fd   (Floor Division)')
print('quit (Close Program)')

operation = input('Select an option: ')

if operation == 'add':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
	print(number_1, "+", number_2, "=", number_1 + number_2)

elif operation == 'sub':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
	print(number_1, '-', number_2, '=', number_1 - number_2)

elif operation == 'mul':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
	print(number_1, 'x', number_2, '=', number_1 * number_2)

elif operation == 'div':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
	print(number_1, '÷', number_2, '=', number_1 / number_2)

elif operation == 'pow':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
	print(number_1, '^', number_2, '=', number_1 ** number_2)

elif operation == 'sq':
        number = int(input('Enter your number: '))
	import math
	print('√', number, '=', math.sqrt(number))
        
elif operation == 'mod':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
	print(number_1, '%', number_2, '=', number_1 % number_2)
        
elif operation == 'fd':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
	print(number_1, '//', number_2, '=', number_1 // number_2)

elif operation == 'quit':
	exit()

else:
        exit()

input('Press enter to quit')

Links:
# https://www.digitalocean.com/community/tutorials/how-to-make-a-simple-calculator-program-in-python-3
# https://www.programiz.com/python-programming/examples/calculator
# https://en.wikibooks.org/wiki/Python_Programming/Basic_Math
