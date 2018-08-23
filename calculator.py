import math

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
        return math.sqrt(x)

def modulus(x, y):
        return x % y

def floor_division(x, y):
	return x // y

print('')
print('Operations')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')
print('5. Power')
print('6. Square Root')
print('7. Modulus')
print('8. Floor Division')

operation = input('Select an option: ')

if operation == '1':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))

elif operation == '2':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))

elif operation == '3':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))

elif operation == '4':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))

elif operation == '5':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))

elif operation == '6':
        number = int(input('Enter your number: '))
        
elif operation == '7':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
        
elif operation == '8':
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))

else:
        print('You have not typed a valid operator, please run the program again.')

if operation == '1':
        print(number_1, "+", number_2, "=", add(number_1, number_2))

elif operation == '2':
        print(number_1, '-', number_2, '=', subtract(number_1, number_2))

elif operation == '3':
        print(number_1, '*', number_2, '=', multiply(number_1, number_2))

elif operation == '4':
        print(number_1, '/', number_2, '=', divide(number_1, number_2))
        
elif operation == '5':
        print(number_1, '**', number_2, '=', power(number_1, number_2))

elif operation == '6':
        print('√', number, '=', sqaure_root(number))

elif operation == '7':
        print(number_1, '%', number_2, '=', modulus(number_1, number_2))
        
elif operation == '8':
        print(number_1, '//', number_2, '=', floor_division(number_1, number_2))

input('Press enter to quit')

Links:
# https://www.digitalocean.com/community/tutorials/how-to-make-a-simple-calculator-program-in-python-3
# https://www.programiz.com/python-programming/examples/calculator
# https://en.wikibooks.org/wiki/Python_Programming/Basic_Math
