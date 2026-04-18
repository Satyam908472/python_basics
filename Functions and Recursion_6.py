### Functions in python
### A function is a block of code that performs a specific task and can be reused multiple times in a program.
### def keyword is used to define a function in python.

# def calc_sum(a, b): # a and b are parameters of the function
#     sum = a + b
#     return sum
# result = calc_sum(178, 122) # 178 and 122 are arguments passed to the function
# print("The sum is:", result) 

# def print_greeting(name):
#     print("Hello, " + name + "! Welcome to the world of Python programming.")
# print_greeting("Satyam") 
# print_greeting("Alice")
# print_greeting("Bob")   

### calculate the average of three numbers using a function

# def calculate_average(num1, num2, num3):
#     average = (num1 + num2 + num3) / 3
#     return average
# result = calculate_average(94, 95, 98)
# print("the average is:", result)

### Default parameters
### Assigning a default value to parameter, which is used when no argument is passed.

# def calc_product(a, b=8):
#     product = (a * b)
#     print(product)
#     return product
# calc_product(2)

### Write a function to print the length of a list.(list is the parameter)
# cities = ["delhi", "noida", "pune", "mumbai", "chennai", "gurgaon", "bengaluru"]
# fruits = ["apple", "banana", "grapes", "orange", "mango", "papaya", "watermelon", "tamarind"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(fruits)

### Write a function to print the elements of a list in a single line.(list is the parameter)
# fruits = ["apple", "banana", "grapes", "orange", "mango", "papaya", "watermelon", "tamarind"]

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(fruits)
# print()

### Write a function to find the factorial of n.(n is the parameter)
# def calc_facto(n):
#     facto = 1
#     for i in range(1, n+1):
#         facto *= i
#     print(facto)

# calc_facto(6)

### Write a function to convert USD to INR.
# def converter(USD_val):
#     INR_val = USD_val * 93.09
#     print(USD_val, "USD =", INR_val, "INR")
# converter(230)

### write a function to check the number is even or odd.
# def num(n):
#     rem = n % 2
#     if(rem == 0):
#         print("the number is EVEN")
#     else:
#         print("the number is ODD")
# num(56)

### Recursion in python 
### When a function calls itself repeatdly.
### recursive function

# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n - 1)
# show(5)

# def factorial(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))

### Write a recursive function to calculate  the sum of frist n natural numbers.
# def calc_sum(n):
#     if(n == 0 ):
#         return 0
#     return calc_sum(n - 1) + n

# sum = calc_sum(5)
# print(sum)

### Write a recursive function to print all elements in a list.
# def print_list(list, idx = 0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx + 1)

# fruits = ["apple", "banana", "grapes", "orange", "mango", "papaya", "watermelon", "tamarind"]
# print_list(fruits)
 
