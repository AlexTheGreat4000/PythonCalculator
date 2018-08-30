print('Welcome to Calculator')

def add(x, y):
        return x + y

def subtract(x, y):
        return x - y

def multiply(x, y):
        return x * y

def divide(x, y):
        return x / y

def power(x, y):
        return x ** y

def square_root(x):
	import math
        return math.sqrt(x)

def modulus(x, y):
        return x % y

def floor_division(x, y):
	return x // y

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

operation = input('Select an option: ')

if operation == 'add':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))

elif operation == 'sub':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))

elif operation == 'mul':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))

elif operation == 'div':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))

elif operation == 'pow':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))

elif operation == 'sq':
        number = int(input('Enter your number: '))
        
elif operation == 'mod':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
        
elif operation == 'fd':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))

else:
        print('You have not typed a valid operator, please run the program again.')

if operation == 'add':
        print(number_1, "+", number_2, "=", add(number_1, number_2))

elif operation == 'sub':
        print(number_1, '-', number_2, '=', subtract(number_1, number_2))

elif operation == 'mul':
        print(number_1, '*', number_2, '=', multiply(number_1, number_2))

elif operation == 'div':
        print(number_1, '/', number_2, '=', divide(number_1, number_2))
        
elif operation == 'pow':
        print(number_1, '**', number_2, '=', power(number_1, number_2))

elif operation == 'sq':
        print('√', number, '=', sqaure_root(number))

elif operation == 'mod':
        print(number_1, '%', number_2, '=', modulus(number_1, number_2))
        
elif operation == 'fd':
        print(number_1, '//', number_2, '=', floor_division(number_1, number_2))

input('Press enter to quit')

Links:
# https://www.digitalocean.com/community/tutorials/how-to-make-a-simple-calculator-program-in-python-3
# https://www.programiz.com/python-programming/examples/calculator
# https://en.wikibooks.org/wiki/Python_Programming/Basic_Math
