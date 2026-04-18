### dictionary in python
## A dictionary in python are used to store data values in key-value pairs, which is unordered, mutable(changeable) and doesn't allow duplicate keys.
## In Python, dictionaries are written with curly brackets.

# info = {
#     "name": "John",
#     "subject": ["Python", "C++", "Java"],
#     "topics": ("Data Structures", "Algorithms", "Machine Learning"),
#     "age": 20,
#     "major": "Computer Science",
#     "gpa": 3.5,
#     "is_student": True
# }

# print(info)
# print(type(info))   
# print(info["name"])
# print(info["subject"])
# print(info["topics"])
# print(info["age"])  
# print(info["major"])
# print(info["gpa"])
# print(info["is_student"])

# info["name"] = "Alice"
# info["surname"] = "Smith"
# print(info)


# null_dict = {}
# null_dict["name"] = "John"
# print(null_dict)

## nested dictionary

# student_info = {
#     "name": "John",
#     "subject": {
#         "physics": 85,
#         "math": 90,
#         "chemistry": 80
#     }
# }   

# print(student_info)
# print(student_info["name"])
# print(student_info["subject"])
# print(student_info["subject"]["physics"])
# print(student_info["subject"]["math"])
# print(student_info["subject"]["chemistry"])

### dictionary methods
## .keys() - returns a list of all the keys in the dictionary
## .values() - returns a list of all the values in the dictionary
## .items() - returns a list of all the key-value pairs in the dictionary
## .get(key) - returns the value of the specified key
## .update() - updates the dictionary with the specified key-value pairs

# student_info = {
#     "name": "John",
#     "subject": {
#         "physics": 85,
#         "math": 90,
#         "chemistry": 80
#     }
# }
# print(student_info.keys())
# print(student_info.values())
# print(student_info.items())
# print(student_info.get("name"))
# student_info.update({"age": 20})
# print(student_info)

### set in python
## A set in python is an unordered collection of unique items, which is mutable(changeable) and doesn't allow duplicate values.
## but the elements in sets are immutable (cannot be changed).
## In Python, sets are written with curly brackets.

# collection = {1, 2, 2, 3, 4, 5, "Hello", "World", "Hello", 1.5, 2.5, 3.5, (1, 2), (3, 4), (1, 2)}
# print(collection)
# print(type(collection))
# print(len(collection))
  
## empty set
# collecction = set()
# print(collecction)
# print(type(collecction))

## set methods
## .add(x) - adds an item x to the set
## .remove(x) - removes an item x from the set (raises KeyError if x is not found)
## .clear() - removes all items from the set
## .pop() - removes and returns an arbitrary item from the set (raises KeyError if the set is empty)
## .union(set1, set2) - returns a new set that is the union of set1 and set2
## .intersection(set1, set2) - returns a new set that is the intersection of set1 and set2

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add("Hello")
# collection.add("World")
# collection.add(2)
# print(collection)
# print(len(collection))
# collection.remove(2)
# print(collection)
# print(len(collection))
# collection.clear()
# print(collection)
# print(len(collection))

# collection = {"Hello", "World", "Python", "Programming", "Language"}
# print(collection.pop())
# print(collection.pop())

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# print(set1.union(set2))
# print(set1)
# print(set2)
# print(set1.intersection(set2))
# print(set1)
# print(set2)

### Store following word meanings in a python dictionary:

# dictionary = {
#     "cat" : "a small domesticated carnivorous animal",
#     "table" : ["a piece of furniture", "list of facts and figures"],
# }
# print(dictionary)

### You are given a list of subjects for students.Assume one classroom is required for 1 subject.
### how many classrooms are needed by all students?

# subjects = {
#     "python", "java", "c++", "python", "javascript",
#     "java", "python", "java", "c++", "c"
# }
# print(subjects)
# print(len(subjects))96


### write a program to enter marks of 3 subjects from the user and store them in a dictionary. 
### start with an empty dictionary and add one by one. use subject name as key and marks as value.

# marks = {}
# x = int(input("Enter marks for physics: "))
# marks.update({"physics": x})
# x = int(input("Enter marks for math: "))
# marks.update({"math": x})
# x = int(input("Enter marks for chemistry: "))
# marks.update({"chemistry": x})

# print(marks)

### figure out a way to store 9 & 9.0 as  separate values in a set.

# values = {
#     ("int", 9),
#     ("float", 9.0)
# }
# print(values)


