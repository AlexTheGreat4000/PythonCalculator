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

print('Operation.')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')
print('5.Power')

operation = input('Select an option: ')

    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))

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

else:
    print('You have not typed a valid operator, please run the program again.')

input('Press enter to quit')

Links:
# https://www.digitalocean.com/community/tutorials/how-to-make-a-simple-calculator-program-in-python-3
# https://www.programiz.com/python-programming/examples/calculator
