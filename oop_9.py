### Write OOP classes to handle the following scenarios:
## A user can create and view 2D coordinates
## A user can find out the distance between 2 coordinates
## A user can find the distance of a coordinate from origin
## A user can check if a point lies on a given line
## A user can find the distance between a given 2D point and a given line

# class Point:
#     def __init__(self, x, y):
#         self.x_cord = x
#         self.y_cord = y

#     def __str__(self):
#         return '<{}, {}>'.format(self.x_cord, self.y_cord)
    
#     def euclidean_distance(self, other):
#         return ((self.x_cord - other.x_cord) ** 2 + (self.y_cord - other.y_cord) ** 2) ** 0.5
    
#     def distance_from_origin(self):
#         # return (self.x_cord ** 2 + self.y_cord ** 2) ** 0.5
#         return self.euclidean_distance(Point(0, 0))
    
# p1 = Point(2, 5)
# p2 = Point(5, 7)
# print(p1)
# print(p2)
# print(p1.euclidean_distance(p2))    
# print(p1.distance_from_origin())
# print(p2.distance_from_origin())

# class Line:
#     def __init__(self, A, B, C):
#         self.A = A
#         self.B = B
#         self.C = C

#     def __str__(self):
#         return '{}x + {}y + {} = 0'.format(self.A, self.B, self.C)
    
#     def point_on_line(self, point):
#         if self.A * point.x_cord + self.B * point.y_cord + self.C == 0:
#             return "Point lies on the line"
#         else:
#             return "Point does not lie on the line"
        
#     def shortest_distance(self, point):
#         return abs(self.A * point.x_cord + self.B * point.y_cord + self.C) / (self.A ** 2 + self.B ** 2) ** 0.5

# l1 = Line(1, 1, -2)    
# p1 = Point(1, 1)
# print(l1)
# print(p1)
# print(l1.point_on_line(p1))
# print(l1.shortest_distance(p1))

### How objects access attributes

# class Person:

#   def __init__(self,name_input,country_input):
#     self.name = name_input
#     self.country = country_input

#   def greet(self):
#     if self.country == 'india':
#       print('Namaste',self.name)
#     else:
#       print('Hello',self.name)

## how to access attributes
# p1 = Person('Alice','usa')
# p2 = Person('Bob','india')
# print(p1.name)
# print(p2.name)

## how to access methods
# p1.greet()
# p2.greet()

## what if i try to access non-existent attributes
## print(p1.gender) # this will throw an error because gender attribute does not exist in the Person class

### Attribute creation from outside of the class

# p1.gender = "female" # this will create a new attribute gender for the p1 object
# p2.gender = "male" # this will create a new attribute gender for the p2 object
# print(p1.gender) # this will print "female"
# print(p2.gender) # this will print "male"

#### Reference Variables
## Reference variables hold the objects
## We can create objects without reference variable as well
## An object can have multiple reference variables
## Assigning a new reference variable to an existing object does not create a new object

# object without a reference
# class Person:

#   def __init__(self):
#     self.name = 'nitish'
#     self.gender = 'male'

# p = Person()
# q = p

# # Multiple ref
# print(id(p))
# print(id(q))

# # change attribute value with the help of 2nd object
# print(p.name)
# print(q.name)
# q.name = 'ankit'
# print(q.name)
# print(p.name)

# #Pass by reference
# class Person:

#   def __init__(self,name,gender):
#     self.name = name
#     self.gender = gender

# # outside the class -> function
# def greet(person):
#   print(id(person))
#   print('Hi my name is',person.name,'and I am a',person.gender)
#   p1 = Person('ankit','male')
#   return p1

# p = Person('nitish','male') 
# greet(p)

# p1 = greet(p)
# print(p1.name)
# print(p1.gender)

# print(id(p))

#### Encapsulation
### Encapsulation is the concept of bundling data and methods that operate on that data within a single unit (class).
### It also involves restricting direct access to some of an object's components,
### which is a way of preventing unintended interference and misuse of the data.

## instance variables 
## instance variables are variables that belong to a specific object (instance) of a class.
## each object can have different values for these variables, and they are defined inside the class, usually in the __init__ method.

# instance var -> python tutor
# class Person:

#   def __init__(self,name_input,country_input):
#     self.name = name_input
#     self.country = country_input

# p1 = Person('nitish','india')
# p2 = Person('steve','australia')

# print(p1.name)
# print(p2.name)

## Encapsulation

# class Atm:
#     def __init__(self): # constructor function
#         print(id(self)) # id of the object
#         self.pin = ""
#         self.__balance = 0
#         # self.menu()

#     def get_balance(self):
#         return self.__balance

#     def set_balance(self,new_value):
#         if type(new_value) == int:
#             self.__balance = new_value
#         else:
#             print('beta bahot maarenge')

#     def menu(self):
#         user_input = input("""
#         Hi how can i help you?
#         1. Press 1 to creat pin
#         2. Press 2 to change pin
#         3. Press 3 to check balance
#         4. Press 4 to cash withdraw
#         5. Anythinfg else to exit
#        """)
        
#         if user_input == "1":
#             self.create_pin()
#         elif user_input == "2":
#             self.change_pin()
#         elif user_input == "3":
#             self.check_balance()
#         elif user_input == "4":
#             self.cash_withdraw()
#         else:
#             print("Goodbye 👋")

#     def create_pin(self):
#         user_pin = input("Enter new pin: ")
#         self.pin = user_pin

#         user_balance = float(input("Enter initial balance: "))
#         self.__balance = user_balance

#         print("Pin created successfully!")
#         # self.menu()

#     def change_pin(self):
#         old_pin = input("Enter old pin: ")

#         if old_pin == self.pin:
#             new_pin = input("Enter new pin: ")
#             self.pin = new_pin
#             print("Pin changed successfully!")
#             # self.menu()
#         else:
#             print("Incorrect old pin.")
#             # self.menu()

#     def check_balance(self):
#         user_pin = input("Enter your pin: ")

#         if user_pin == self.pin:
#             print("Your balance is", self.__balance)
#         else:
#             print("chal nikal yahan se.")
#             # self.menu()

#     def cash_withdraw(self):       
#         user_pin = input("Enter your pin: ")

#         if user_pin == self.pin:
#             amount = float(input("Enter amount to withdraw: "))

#             if amount <= self.__balance:
#                 self.__balance = self.__balance - amount
#                 print("Please take your cash.")
#                 print("Remaining balance:", self.__balance)
#             else:
#                 print("Insufficient balance.")
#         else:
#             print("Incorrect pin.")
#         # self.menu() 
             
# obj = Atm() # creating an object of the class Atm
# obj.create_pin() # calling the create_pin method to set the pin and initial balance

# obj.get_balance()
# print(obj.get_balance())
# obj.set_balance(10000)
# print(obj.get_balance())  
# obj.cash_withdraw()

### Encapsulation in Python is achieved through the use of access modifiers.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age  # Protected attribute (convention)
#         self.__salary = 0  # Private attribute (name mangling)

#     def get_age(self):
#         return self._age

#     def set_age(self, age):
#         if age > 0:
#             self._age = age

#     def get_salary(self):
#         return self.__salary

#     def set_salary(self, salary):
#         if salary > 0:
#             self.__salary = salary

# # Example usage
# p = Person("Alice", 30)
# print(p.name)
# print(p.get_age())
# p.set_age(31)
# print(p.get_age())
# print(p.get_salary())
# p.set_salary(50000)
# print(p.get_salary())

### Collection of objects

## list of objects
# class Person:

#   def __init__(self,name,gender):
#     self.name = name
#     self.gender = gender

# p1 = Person('nitish','male')
# p2 = Person('ankit','male')
# p3 = Person('ankita','female')

# L = [p1,p2,p3]

# for i in L:
#   print(i.name,i.gender)

## dict of objects

# class Person:

#   def __init__(self,name,gender):
#     self.name = name
#     self.gender = gender

# p1 = Person('nitish','male')
# p2 = Person('ankit','male')
# p3 = Person('ankita','female')

# d = {'p1':p1,'p2':p2,'p3':p3}

# for i in d:
#   print(d[i].gender)

### Static Variables Vs (Instance variables) 
## Static variables are shared among all instances of a class, while instance variables are unique to each instance.

# class Atm:

#   __counter = 1

#   # constructor(special function)->superpower -> 
#   def __init__(self):
#     self.cid = Atm.__counter
#     Atm.__counter = Atm.__counter + 1


#   ##utility functions
#   @staticmethod
#   def get_counter():
#     return Atm.__counter

# cid1 = Atm()
# print(cid1.cid)
# cid2 = Atm()
# print(cid2.cid)
# cid3 = Atm()
# print(cid3.cid)


