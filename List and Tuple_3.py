### List in Python
## A list is a collection of items stored in a single variable, which is ordered and changeable. 
## In Python, lists are written with square brackets.

## Example of a list
# marks = [94.4, 87.5, 95.2, 66.8, 78.9]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])

## List can contain different data types

# student = ["John", 20, "Computer Science", 3.5]
# print(student)
# print(type(student))
# print(len(student))
# print(student[0])
# print(student[1])

## List can also contain other lists (nested lists)

# nested_list = [1, 2, [3, 4], 5]
# print(nested_list)
# print(nested_list[2])
# print(nested_list[2][0])
# print(nested_list[2][1])

## list can be modified (changeable)

# marks = [94.4, 87.5, 95.2, 66.8, 78.9]
# print(marks)
# marks[0] = 90.0
# marks[1] = 85.0
# marks[4] = 97.5
# print(marks)

## List can be sliced (access a range of items)

# marks = [94.4, 87.5, 95.2, 66.8, 78.9]
# print(marks[1:4]) # from index 1 to index 3 (4 is not included)
# print(marks[:3]) # from the beginning to index 2 (3 is not included)
# print(marks[2:]) # from index 2 to the end
# print(marks[-3:]) # from the third last to the end
# print(marks[:-2]) # from the beginning to the third last (not included)
# print(marks[::2]) # from the beginning to the end with a step of 2
# print(marks[1::2]) # from index 1 to the end with a step of 2

### List Methods
## List methods are built-in functions that can be used to perform various operations on lists.

## list.append(x) - adds an item x to the end of the list
# marks = [94.4, 87.5, 95.2, 66.8, 78.9]
# marks.append(85.0)
# print(marks)

## list.sort() - sorts the list in ascending order
# marks = [94.4, 87.5, 95.2, 66.8, 78.9]
# marks.sort()
# print(marks)

## list.sort(reverse=True) - sorts the list in descending order

# marks = [94.4, 87.5, 95.2, 66.8, 78.9]
# marks.sort(reverse=True)
# print(marks)

### list.reverse() - reverses the order of the list

# marks = [94.4, 87.5, 95.2, 66.8, 78.9]
# marks.reverse()
# print(marks)

### list.insert(i, x) - inserts an item x at a given position i

# marks = [94.4, 87.5, 95.2, 66.8, 78.9]
# marks.insert(2, 90.0) # insert 90.0 at index 2
# print(marks)

### list.remove(x) - removes the first item x from the list

# marks = [94.4, 87.5, 95.2, 66.8, 78.9]
# marks.remove(66.8) # remove the first occurrence of 66.8
# print(marks)

### list.pop(i) - removes the item at the given position i and returns it

# marks = [94.4, 87.5, 95.2, 66.8, 78.9]
# removed_mark = marks.pop(2) # remove the item at index 2 and return
# print(removed_mark)
# print(marks) 

### tuple in Python
## A tuple is a collection of items stored multiple values in a single variable, which is ordered and unchangeable.
## In Python, tuples are written with round brackets.

# tup = (1, 2, 3, 4, 5)
# print(tup)
# print(type(tup))
# print(len(tup)) 
# print(tup[0])
# print(tup[1])
# print(tup[2])

# tup = ()
# print(tup)
# print(type(tup))

# tup = (1,)
# print(tup)
# print(type(tup))

## silicing in tuple
# tup = (1, 2, 3, 4, 5)
# print(tup[1:4]) # from index 1 to index 3 (4 is not included)
# print(tup[:3]) # from the beginning to index 2 (3 is not included)
# print(tup[2:5]) # from index 2 to index 4 (5 is not included)
# print(tup[-3:5]) # from the third last to the end
# print(tup[0:-2]) # from the beginning to the third last (not included)
# print(tup[::2]) # from the beginning to the end with a step of 2
# print(tup[1::2]) # from index 1 to the end with a step of 2

### tuple methods
## tuple.count(x) - returns the number of times x appears in the tuple
## tuple.index(x) - returns the index of the first occurrence of x in the tuple

# tup = (1, 2, 3, 4, 5, 2, 3)
# print(tup.count(2)) # count the number of times 2 appears in the tuple
# print(tup.index(3)) # find the index of the first occurrence of 3 in the tuple

### write a program to ask the user to enter name of their 3 favorite movies and store them in a list.

# movies = [] # create an empty list to store the movies
# movies.append(input("Enter the name of your first favorite movie: "))
# movies.append(input("Enter the name of your second favorite movie: "))
# movies.append(input("Enter the name of your third favorite movie: "))

# print("Your favorite movies are: ", movies)

### Write a program to check if a list contain a palindrome of elements. (Hint: use copy() method)

# list1 = [1, 2, 3, 2, 1]

# copy_list1 = list1.copy() # create a copy of list1
# copy_list1.reverse() # reverse the copy of list1
# if(copy_list1 == list1): # check if the reversed copy is equal to the original list
#     print("list1 is a palindrome")
# else:
#     print("list1 is not a palindrome")

### Write a program to count the number of students with the "A" grade in the following tuple.

# grades = ("A", "B", "C", "A", "B", "A", "C", "B", "A")
# count_A = grades.count("A") # count the number of times "A" appears in the tuple
# print("Number of students with A grade: ", count_A)

### Store the above values in a list and sort them from "A" to "D".

# grades = ["A", "B", "C", "A", "B","D", "A", "C", "B", "D", "A"]
# grades.sort() # sort the list in ascending order
# print("Sorted grades: ", grades)




