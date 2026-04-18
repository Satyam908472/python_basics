### loops in python
### loops are used to repeat a block of code multiple times until a condition is met.

## while loop
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# print("while loop ended")

### Print the numbers from 1 to 100.
# i = 1
# while i <= 100:
#     print(i)
#     i += 1
# print("while loop ended")

### Print the numbers from 100 to 1.
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1  
# print("while loop ended")

### Print the multiplication table of a number n.
# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:    
#     print(n * i)
#     i += 1    
# print("while loop ended")

# n = 3
# i = 1
# while i <= 10:
#     print(n * i)
#     i += 1
# print("while loop ended")

### Print the elements of the following list using  a while loop.
### [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1
# print("while loop ended")

### Search for a number x in this tuple using a while loop.
### nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("Enter a number to search: "))
# i = 0
# while i < len(nums):
#     if (nums[i] == x):
#         print("Number found in the tuple at index", i)
#     i += 1
# print("while loop ended")

### Break and continue statements in while loop
### break statement is used to exit the loop when a certain condition is met.
# i = 1
# while i <= 10:
#     print(i)
#     if (i == 6):
#         break
#     i += 1
# print("while loop ended")

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
# x = int(input("Enter a number to search: "))
# i = 0
# while i < len(nums):
#     if (nums[i] == x):
#         print("Number found in the tuple at index", i)
#         break
#     i += 1
# print("while loop ended")

### continue statement is used to skip the current iteration of the loop when a certain condition is met.
# i = 1
# while i <= 10:
#     if (i == 6):
#         i += 1
#         continue
#     print(i)
#     i += 1
# print("while loop ended")

# i = 1 
# while i <= 10:
#     if (i % 2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1
# print("while loop ended")

### for loop
### for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for val in list:
#     print(val)

# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 200)
# for num in tup:
#     print(num)

# str = "Satyam Pandey"
# for char in str:
#     print(char)

### Print the elements of the following list using a for loop.
### [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 25]
# for el in nums:
#     print(el)

### Search for a number x in this tuple using a for loop.
### nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
# x = int(input("Enter a number to search: "))
# i = 0
# for el in nums:
#     if (el == x):
#         print("Number found in the tuple at index", i)
#     i += 1
# print("for loop ended")

### Range function in for loop
### range function returns a sequence of numbers.
### start from 0 by default, and increments by 1 (by default), and stops before a specified number.
### It takes three arguments: start, stop, and step.

# seq = range(10) # start from 0, stop before 10, and increment by 1 (by default)
# for i in seq:
#     print(i)

# for i in range(2, 11): # start from 2, stop before 11, and increment by 1 (by default)
#     print(i)

# for i in range(2, 11, 2): # start from 2, stop before 11, and increment by 2
#     print(i)

# for i in range(2, 100, 2): # start from 2, stop before 100, and increment by 2
#     print(i)
 
### Print the numbers from 1 to 100 using a for loop and range function.
# for i in range(1, 101): # start from 1, stop before 101, and increment by 1 (by default)
#     print(i)

### Print the numbers from 100 to 1 using a for loop and range function.
# for i in range(100, 0, -1): # start from 100, stop before 0, and decrement by 1
#     print(i)

### Print the multiplication table of a number n using a for loop and range function.
# n = int(input("Enter a number: "))
# for i in range(1, 11): # start from 1, stop before 11, and increment by 1 (by default)
#     print(n * i)

### Pass statement
### Pass is a null statement that does nothing. It is used as a placeholder for future code.

# for i in range(1, 11):
#     pass
# print("some useful work can be done here")

### Write a program to find the sum of first n natural numbers. (using while loop)

# n = int(input("Enter a number: "))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print("The sum of first", n, "natural numbers is:", sum)

### Write a program to find the factorial of first n natural numbers. (using for loop)

# n = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print("The factorial of", n, "is:", factorial)



