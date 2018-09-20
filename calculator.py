print("""Operations
1. (Addiction)
2. (Subtraction)
3. (Multiplication)
4. (Division)
5. (Power)
6. (Sqaure Root)
7. (Modulo)
8. (Floor Division)
q  (Close Program)""")
operation = input("Select an operation: ")
if operation=="6":
	number=float(input("Enter your number: "))
elif operation=="q":
	exit()
else:
	number1=float(input("Enter your first number: "))
	number2=float(input("Enter your second number: "))
if operation=="1":
	print(number1,"+",number2,"=",number1+number2)
elif operation=="2":
	print(number1,"-",number2,"=",number1-number2)
elif operation=="3":
	print(number1,"x",number2,"=",number1*number2)
elif operation=="4":
	print(number1,"÷",number2,"=",number1/number2)
elif operation=="5":
	print(number1,"^",number2,"=",number1**number2)
elif operation=="6":
	import math
	print("√",number,"=",math.sqrt(number))
elif operation=="7":
	print(number1,"mod",number2,"=",number1%number2)
elif operation=="8":
	print(number1,"//",number2,"=",number1//number2)
input("Press enter to exit")
