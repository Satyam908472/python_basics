### First Python Program

# print("Hello, World!")
# print("My name is Satyam Pandey.")
# print("I am a student of Computer Science.")

### Variables in Python
## A variable is a named storage location in memory used to store data that can be changed during program execution.
## In Python, you can create a variable by simply assigning a value to it.

# name = "Satyam Pandey" # This is a string variable that stores the name "Satyam Pandey"
# age = 20
# price = 19.99
# #age2 = age
# print("My name is :", name)
# print(age)
# #print(age2)
# print(price)
      
# print(type(name))
# print(type(age))
# print(type(price))

### Data Types in Python
### Python has several built-in data types, including:
## - int: Represents integer numbers (e.g., 1, 42, -5)
## - float: Represents floating-point numbers (e.g., 3.14, -0.001)
##- str: Represents strings of characters (e.g., "Hello", 'Python') 
## - bool: Represents boolean values (True or False)
## - list: Represents ordered collections of items (e.g., [1, 2, 3], ["apple", "banana"])
## - none: Represents the absence of a value (None)

# age = 20
# height = 5.9
# name = "Satyam Pandey"
# is_student = True
# favorite_colors = ["red", "blue", "green"]
# a = None
# print(type(age))
# print(type(height)) 
# print(type(name))
# print(type(is_student))
# print(type(favorite_colors))
# print(type(a))

### Print sum & difference of two numbers

# a = 1000
# b = 500
# sum = a + b
# diff = a - b
# print("Sum:", sum)
# print("Difference:", diff)

### Arthimatic operators

# a = 5
# b = 2 

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b) #modulus operator (remainder of the division)
# print(a//b) #floor division (quotient without decimal part)
# print(a**b) #exponentiation a^b          

### Relational operators

# a = 50
# b = 20

# print(a > b) #greater than
# print(a < b) #less than
# print(a >= b) #greater than or equal to
# print(a <= b) #less than or equal to
# print(a == b) #equal to
# print(a != b) #not equal to

### Assignment operators

# num = 10
# num += 5 # num = num + 5
# print("num =", num) #15

# num = 10
# num -= 3 # num = num - 3
# print("num =", num) #7
 
# num = 10
# num *= 5 # num = num * 5
# print("num =", num) #50

# num = 10
# num /= 5 # num = num / 5
# print("num =", num) #2.0

# num = 10
# num %= 5 # num = num % 5
# print("num =", num) #0

# num = 10
# num **= 5 # num = num ** 5
# print("num =", num) #100000

### Logical operators

# a = 50
# b = 30
# print(not False) #True
# print(not (a > b)) #False

# val1 = True
# val2 = False
# print("AND operator:", val1 and val2) #False
# print("OR operator:", val1 or val2) #True
# print("OR operator:", (a == b) or (a > b)) #True

### Type conversion 

# a = 2
# b = 4.25
# sum = a + b # 2.0 + 4.25 = 6.25
# print("Sum:", sum) #6.25

### Type casting

# a = int("2")
# b = 4.25
# print(type(a)) #<class 'int'>
# print(a + b) #6.25

### User input in python

#input("Enter your name: ") # This will prompt the user to enter their name, but it won't store the input in a variable.
# name = input("Enter your name: ")
# print("Welcome ", name)

# val = input("Enter some value: ")
# print(type(val), val)

# val = int(input("Enter a number: "))
# print(type(val), val)

### Write a program to input 2 numbers and print their sum

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# sum = num1 + num2 
# print("Sum:", sum)

### Write a program to input side of a square and print its area

# side = float(input("Enter the side of the square: "))
# area = side ** 2
# print("Area of the square:", area)

### Write a program to input 2 floating point numbers and print their average

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# average = (num1 + num2) / 2
# print("Average:", average)

### Write a program to input 2 int numbers a and b. Print true if a is greater than or equal to b. if not print false.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(a >= b)

# if a >= b:
#     print("True")
# else:    
#     print("False")   


