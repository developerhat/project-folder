#Python calculator.. WORKS,, Need to add exception handler cos EMAN broke with 50/0.

#This function is for addition
def add(x, y):
   return x + y

#Function for subtraction
def subtract(x, y):
   return x - y

#Function for multiplication
def multiply(x, y):
   return x * y

#Function for division
def division(x, y):
   return x / y
print("Welcome to Patrick's calculator! ")
print('\n' * 4)
print("Enter 1 for addition ")
print("Enter 2 for subtraction ")
print("Enter 3 for multiplication ")
print("Enter 4 for division ")

#choice = input("Please enter your desired operation 1/2/3/4: ")
choice = ''
options = ['1', '2', '3', '4']
while choice not in options:
    choice = input("Please enter your desired operation 1/2/3/4: ")

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

if choice == '1':
   print(num1, "+", num2, "=", add(num1,num2))

elif choice == '2':
  print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
  print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
  print(num1,"/",num2,"=", division(num1,num2))

else:
  print("Invalid input")
