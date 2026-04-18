### Strings in Python
## A string is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).

# str1 = 'Hello, World!'
# str2 = "Python is great!"
# str3 = """This is a multi-line string."""

# print(str1)

# str4 = 'Hello, World! \nThis is a multi-line string.'
# print(str4)

### String concatenation

# str5 = "Satyam"
# len1 = len(str5)
# print(len1)
# str6 = "Pandey"
# len2 = len(str6)
# print(len2)
# full_str = str5 + " " + str6 ## Concatenating str5 and str6 with a space in between
# print(full_str)
# print(len(full_str)) 

### String indexing 

# str7 = "Satyam Pandey" # Indexing starts from 0
# print(str7[0]) 
# print(str7[8]) 

### String slicing

# str = "Satyam Pandey"
# print(str[0:6]) # Satyam
# print(str[7:13]) # Pandey
# print(str[:6]) # Satyam 
# print(str[7:]) # Pandey
# print(str[:]) # Satyam Pandey

# str = "apple"
# print(str[-5:-1])

### String Functions
## str.endswith() - Checks if the string ends with a specified suffix
## str.startswith() - Checks if the string starts with a specified prefix
## str.upper() - Converts all characters in the string to uppercase
## str.lower() - Converts all characters in the string to lowercase

# str = "I am learning python programming language and it is very interesting."
# print(str.endswith("interesting.")) 
# print(str.startswith("am"))
# print(str.upper())
# print(str.lower())

## str.capitalize() - Capitalizes the first character of the string and converts the rest to lowercase

# str = "i am learning python programming language and it is very interesting."
# print(str.capitalize())

## str.replace() - Replaces a specified substring with another substring

# str = "I am learning python programming language and it is very interesting."
# print(str.replace("python", "Java"))

## str.find() - Returns the lowest index of the substring if it is found in the string, otherwise returns -1

# str = "I am learning python programming language and it is very interesting."
# print(str.find("python"))

## str.count() - Returns the number of occurrences of a specified substring in the string

# str = "I am learning python programming language and it is very interesting."
# print(str.count("python"))

## str.split() - Splits the string into a list of substrings based on a specified delimiter (default is whitespace)

# str = "I am learning python programming language and it is very interesting."
# print(str.split())

### Write a program to input user's first name & print its length.

# first_name = input("Enter your first name: ")
# print("Length of your first name is:", len(first_name))

### Write a program to find the occurence of '$' in the given string.

# str = "I have $$$$100 in my wallet ."
# print("The occurrence of '$' in the string is:", str.count('$'))

### Conditional Statements in Python
## Conditional statements allow you to execute different blocks of code based on certain conditions. 
## The main conditional statements in Python are if, elif, and else.

# light = input("Is the traffic light is: ")
# if (light == "red"):
#     print("Stop")
# elif (light == "yellow"):
#     print("Get ready")
# elif (light == "green"):
#     print("Go")
# else:
#     print("Invalid traffic light color")

# num = 5
# if (num > 2):
#     print("greater than 2")
# if (num > 3):
#     print("greater than 3")

# age = 24
# if (age >= 18):
#     print("You are an adult.")
# else:
#     print("You are a minor.")

# marks = int(input("Enter your marks: "))
# if (marks >= 90):
#     print("Grade: A")
# elif (marks >= 80 and marks < 90):
#     print("Grade: B")
# elif (marks >= 70 and marks < 80):
#     print("Grade: C")
# elif (marks >= 60 and marks < 70):
#     print("Grade: D")
# else:    
#     print("Grade: F")  

### Nesting of if statements

# age = int(input("Enter your age: "))
# if (age >= 18):
#     print("You are an adult.")
#     if (age >= 21):
#         print("You can also drink alcohol.")
#     else:
#         print("You cannot drink alcohol.")

### Write a program to check if a number entered by the user is even or odd.

# num = int(input("Enter a number: "))
# rem = num % 2
# if (rem == 0):
#     print("The number is even.")
# else:
#       print("The number is odd.")

### Write a program to find the greatest of 4 numbers entered by the user.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# num4 = int(input("Enter fourth number: "))
# if (num1 >= num2 and num1 >= num3 and num1 >= num4):
#     print("The greatest number is:", num1)
# elif (num2 >= num1 and num2 >= num3 and num2 >= num4):
#     print("The greatest number is:", num2)
# elif (num3 >= num1 and num3 >= num2 and num3 >= num4):
#     print("The greatest number is:", num3)
# else:
#     print("The greatest number is:", num4)

### Write a program to check if a number is a multiple of 7 or not.

# num = int(input("Enter a number: "))
# rem = num % 7
# if (rem == 0):
#     print("The number is a multiple of 7.") 
# else:
#     print("The number is not a multiple of 7.")


