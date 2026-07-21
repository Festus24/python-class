"""
module 7: Function
defining and calling function
parameters and arguments
REturn values
Default arguments
positional and keyward argument
parametized and unparametized fuction
variable scope (local and global)
Advanced function concepts
*args and **kwargs
Lambda functions
Writing doc-strings and documentation

"""
# Function definition
# def message(): 
#     print("I am a python developer,")
# # message()  # function invocation or calling

# def student_record(name, score):
#     print(f"My name is {name} and my score is {score}")
# # student_record("Samuel", 90) # Samuel abd score are the argument

# # Return values
# def addintion(y, x):
#     return y + x
# # print(addintion(10, 15))

# # Default arguments
# def calculator(val1=23, val2=10, val3=3):
#     return f"Total value: {val1 + val2 + val3}"
# # print(calculator())
# # print(calculator(5, 2, 3))

# # Positional argument
# def student_record(name, score): #name and score are the parameters
#     print(f"My name is {name} and my score is {score}")
# # student_record(90, "Samuel") # Samuel and 90 are the argument


# # Keyword argument
# def item_price(name, price, quantity):
#     print(f"the total price of {name} is {price * quantity}")
# # item_price(quantity=2, price=1000, name="Rice")

# def message(name): # function definition
#     print(f"My name is {name}, I am a python developer")
# # message(name=input("Eneter your name: "))

# # Variable scope (Local)
# def my_record():
#     name = "James"
#     gender = input("Enter your gender: ")
    
#     return f"My name is {name}, I am a {gender}"
# # print(my_record())

# # Variable scope (Global)
# number = [10, 23, 5, 60]
# total = 0
# def sum_price():
#     global total
#     for price in number:
#         total+=price
#     print(total)
# # sum_price()

"""
Calcutator
"""

# def addition():
#     val1 = int(input("Enter val1: "))
#     val2 = int(input("Enter val2: "))
#     print(val1 + val2)

# def subtraction():
#     val1 = int(input("Enter val1: "))
#     val2 = int(input("Enter val2: "))
#     print(val1 - val2)

# def multiplication():
#     val1 = int(input("Enter val1: "))
#     val2 = int(input("Enter val2: "))
#     print(val1 * val2)

# def Division():
#     val1 = int(input("Enter val1: "))
#     val2 = int(input("Enter val2: "))
#     print(val1 / val2)

# def landing_page():
#     while True:
#         print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. exit")
    
#         user = input("Enter your choice: ")
#         if user == "1":
#             addition()
    
#         elif user == "2":
#             subtraction()
    
#         elif user == "3":
#             multiplication()
    
#         elif user == "4":
#             Division()
    
#         elif user == "5":
#             break
# landing_page()

"""
Artbitary argument
"""
# def student_score(name, *args):
#     print("name: ", name)
#     total = sum(args)
#     print(f"Total score: {total}")
#     print(f"AVG: {total/len(args):.2f}")
#     return args

# print(student_score("Oba", 80, 50, 60, 85, 90, 78))
# print(student_score("Samuel", 76, 30, 50, 81, 65, 79))

# item_price = [100, 150, 1000, 25000]
# total = 0
# def total_price(*p):
#     global total
#     for price in item_price:
#         total+=price
        
#     print("Total", total)
# total_price()

"""
Arbitary key argument(**Kwargs)
"""
# def employee_info(**kwargs):
#     # return kwargs
#     for k, v in kwargs.items():
#         print(f"{k}: {v}")

# employee_info(name='Oba', department="HR", age=55, salary="1.5M")

# def student_rd(*score, **student_information):
#     print("args: ", score)
#     print("kwargs: ", student_information)
# student_rd(50, 60, 70, 56, 76, name="John", matric_no=202645, department= "Physics")

# list_num = [2, 3, 6, 9, 11, 1, 4, 7]
# expensive = list(filter(lambda i: i%2==0, list_num))
# print(expensive)


# val1 = 10
# x = lambda i: i%2==0
# print(x(val1))

# list_num = [2, 3, 6, 9, 11]
# even = lambda num: num%2==0
# print(even(list_num))

# def x(i):
#     return i%2==0
# print(x(val1))

# l="Mango"
# s = lambda r: len(r)
# print(s(l))

# employees = [
#     {"name": "John", "salary": 60000},
#     {"name": "Mary", "salary": 45000},
#     {"name": "Ayomide", "salary": 75000},
#     {"name": "Oba", "salary": 750000},
#     {"name": "Fatimah", "salary": 1500000},
# ]

# employees.sort(key=lambda emp: emp["salary"])
# print(employees)

# prices = [12000, 80000, 45000, 150000, 30000, 60000, 10000, 25000]
# expensive = list(filter(lambda price: price > 50000, prices))
# print(expensive)

# names = ["Samuel" "Fatimah", "Festus", "Emmanuel", "Ibrahim", "Kenny", "David", "Samuel"]
# student_name = list(filter(lambda name: len(name)<=6, names))
# print(student_name)