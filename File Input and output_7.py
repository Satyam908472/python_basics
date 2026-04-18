### File input/output in python
### Pyhton can be used to perform operations on a file. (read & write data)
### reading to a file

# f = open("demo.txt", "r")
# data = f.read() # reads entire line
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt", "r")
# data = f.read(5) # reads the particular sets characters
# print(data)
# f.close()

# f = open("demo.txt", "r")
# line1 = f.readline() # reads one line at a time
# print(line1)
# line2 = f.readline()
# print(line2)
# f.close()

### writing to a file

# f = open("demo.txt", "w")
# f.write("Hello, to day i am learning python 123456.") # "w" used to overwrites  the entire file
# f.close()

# f = open("demo.txt", "a")
# f.write("\nAfter that machine learning.") # "a" adds to the file
# f.close

# f = open("demo.txt", "r+") # "r+" is used to read and write (pointer at start & no truncate)
# f.write("abc") 
# print(f.read())
# f.close()

# f = open("demo.txt", "w+")  # "w+" is used to write and read (truncate)
# print(f.read())
# f.write("abcd")
# f.close()

# f = open("demo.txt", "a+")  # "a+" is used to read and append (pointer at end & no truncate)
# print(f.read())
# f.write("abcd")
# f.close()

### with syntax
### read mode
# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

### write mode
# with open("demo.txt", "w") as f:
#     f.write("I am learning python")

### Deleting a file
### using the os module
### module (like a code library) is a file written by another programmer that generally has a functions we can use.

# import os
# os.remove("sample.txt")

### create a new file "practice.txt" using python. Add the following data in it:
# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\n")
#     f.write("using Python.\nI like programming in Python.")

### Write a function that replace all occurrences of "Python" with "Java" in above file: 
# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("Python", "Java")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)

### Search if the word "learning" exists in the file or not:
# word = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not Found")

### Write a function to find in which line of the file does the word "learning" occure first:
# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1

#     return-1        

# check_for_line()

### From a file containing numbers separated by comma, print the count of even numbers:
# count = 0
# with open("practice.txt", "r") as f:
#     data = f.read()

#     nums = data.split(",")
#     for val in nums:
#         if(int(val) % 2 == 0):
#             count += 1

# print(count)            

  


