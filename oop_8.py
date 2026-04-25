#### OOP is a way of writing programs by creating classes (blueprints)
### and objects (real instances) that contain both data (attributes) and functions (methods).
#### In OOP, we can model real-world entities as classses,
### and then create objects from those classes to represent specific instances of those entities.

#### class & objects in python
### class is a blueprint for creating objects, and an object is an instance of a class.

### syntax of creating a class in ptthon

# class Studant:  # creating class
#     name = "John Doe"

# s1 = Studant()  # creating an object of the class Studant
# print(s1)
# print(s1.name)

# class Car:
#     color = "Black"
#     brand = "Toyota"

# car1 =Car()
# print(car1.color)
# print(car1.brand) 

### syntax of creating a object in python
### objectname = classname()
## object literal
# l = list() 
# l = [1, 2, 3, 4, 5, 6, 7] # list is a class in python and l is an object of that class
# s = str()

#### Constructor in python (__init__ function)
### All classes have a function called __init__(), which is always executed when the object of the class is being initiated.
### It is used to initialize the attributes of the class.

### Pascal Case
### The frist letter of each word is capitalized and there are no spaces between the words.
## HelloWorld, MyClass

# class Atm:
#     def __init__(self): # constructor function
#         print(id(self)) # id of the object
#         self.pin = ""
#         self.balance = 0
#         self.menu()

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
#         self.balance = user_balance

#         print("Pin created successfully!")
#         self.menu()

#     def change_pin(self):
#         old_pin = input("Enter old pin: ")

#         if old_pin == self.pin:
#             new_pin = input("Enter new pin: ")
#             self.pin = new_pin
#             print("Pin changed successfully!")
#             self.menu()
#         else:
#             print("Incorrect old pin.")
#             self.menu()

#     def check_balance(self):
#         user_pin = input("Enter your pin: ")

#         if user_pin == self.pin:
#             print("Your balance is", self.balance)
#         else:
#             print("chal nikal yahan se.")
#             self.menu()

#     def cash_withdraw(self):       
#         user_pin = input("Enter your pin: ")

#         if user_pin == self.pin:
#             amount = float(input("Enter amount to withdraw: "))

#             if amount <= self.balance:
#                 self.balance = self.balance - amount
#                 print("Please take your cash.")
#                 print("Remaining balance:", self.balance)
#             else:
#                 print("Insufficient balance.")
#         else:
#             print("Incorrect pin.")
#         self.menu() 
             
# obj = Atm() # creating an object of the class Atm

 
### Methods Vs Functions
### L = [1, 2, 3, 4, 5]
### len(L) # function because it is outside the class
### L.append(6) # method because it is inside the class

### Create a class called Fraction that represents a fraction with a numerator and denominator.
### creating a data type for fraction and performing basic arithmetic operations on it.

# class Fraction:

#   # parameterized constructor
#   def __init__(self,x,y):
#     self.num = x
#     self.den = y

#   def __str__(self):
#     return '{}/{}'.format(self.num,self.den)

#   def __add__(self,other):
#     new_num = self.num*other.den + other.num*self.den
#     new_den = self.den*other.den

#     return '{}/{}'.format(new_num,new_den)

#   def __sub__(self,other):
#     new_num = self.num*other.den - other.num*self.den
#     new_den = self.den*other.den

#     return '{}/{}'.format(new_num,new_den)

#   def __mul__(self,other):
#     new_num = self.num*other.num
#     new_den = self.den*other.den

#     return '{}/{}'.format(new_num,new_den)

#   def __truediv__(self,other):
#     new_num = self.num*other.den
#     new_den = self.den*other.num

#     return '{}/{}'.format(new_num,new_den)

#   def convert_to_decimal(self):
#     return self.num/self.den
  
# f1 = Fraction(3, 4)
# f2 = Fraction(1, 2)
# print(f1) # 3/4
# print(f2) # 1/2
# print(f1+f2)
# print(f1-f2)
# print(f1*f2)
# print(f1/f2)
# print(f1.convert_to_decimal())

  
