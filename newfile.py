from colorama import init
from colorama import Fore, Back, Style
print(Back.CYAN )
print(Fore.BLACK)
what=input("Какое действие выполнить? '+' '-' '/' '*'")

num1=input("Первое число: ")
num2=input("Второе число: ")
print(Back.GREEN)
if what=="+":
	c=float(num1)+float(num2)
	print( c )
elif what=="-":
	c=float(num1)-float(num2)
	print(c)
elif what=="/":
	c=float(num1)/float(num2)
	print(c)
elif what=="*":
	c=float(num1)*float(num2)
	print(c)
else:
	print(Back.RED)	
	print("Иди нахуй")
input()
