"""
Tuple
"""
tuple1 = ()
tuple1 = (())
tuple3 = tuple([])
fruit_name = ('orange', True, 2.9, 'Apple', False, 100, 3j)
# fruit_name2 = ("cherry",)
# print(type(fruit_name2))
# print(fruit_name)
# print(fruit_name[3])

# fruit_name[3] = "Mango"
# print(fruit_name)
# print(fruit_name[3:5])

# for element in fruit_name:
#     print(type(element))

# Tuple methods
# print(fruit_name.count("Apple"))
# print(fruit_name.index("Apple"))
# print(fruit_name.__add__(("Cherry","Apple")))
# print(fruit_name.__len__())
# print(fruit_name.__doc__)

"""
Nested tuple
"""

# student_record = [["Oba", "Cyber", 20265], ["Festus", "Native app", 20266], ["Kenny", "Network appl", 20266]]

# fruit_name = ('orange', True, 2.9, 'Apple', False, 100, 3j)
# my_list = list(fruit_name)
# my_list[3] = "Date"

# my_tuple = tuple(my_list)
# print(my_tuple)

"""
Python Dictionary
"""
my_dict1 = {}

# creating dictionary using constructor
# my_dict2 = dict(())
# my_dict3 =  dict([])

# Dictionary creation and manipulation
item_list = {"Bournvita": 100, "Peak milk": 1500, "Sugar":500, "Bread":300}
# print(item_list["Bread"])

# Dictionary methods
# item_list.clear()
# print(item_list)
# print(item_list.get("Bread"))
# print(item_list.keys())
# print(item_list.fromkeys("Bread", 100))
# print(item_list.items())
# item_list.update({"sugar":100})
# print(item_list)

"""
Nested data structures
"""
# student_record = {"name":"Festus", "Gender":["Male", "Female"], "Nigeria":{"state":"Oyo"}}
# print(student_record["Gender"][1])

cbt_test = {
    1:{"Question": "Which of the following is domestic animals?", "Option":["A. Lion", "B. Elephant", "c. Dog"], "Answer": "C"},
    2:{"Question": "Which of the following is wild animals?", "Option":["A. Lion", "B. Cat", "c. Dog"], "Answer": "A"}
}
#
# print(cbt_test[1])
score = 0

for each, quest in cbt_test.items():
    print(f"{each}. {quest["Question"]}")
    
    for opt in quest["Option"]:
        print(opt)
    
    user_input = input("Select ypur option>> ").capitalize()
    
    if user_input == quest["Answer"]:
        print("correct\n")
        score+=5
        
    else:
        print("incorrect\n")
print(f"Total score: {score}")















