print('Welcome to Calculator')

print('Operation.')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')

operation = input('Select an option: ')

    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))

if operation == '1':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '2':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '3':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '4':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('You have not typed a valid operator, please run the program again.')


def again():

    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again == 'Y':
        calculate()
        
    elif calc_again == 'N':
        print('See you later.')

    else:
        again()

again()

Links:
# https://www.digitalocean.com/community/tutorials/how-to-make-a-simple-calculator-program-in-python-3
# https://www.programiz.com/python-programming/examples/calculator
