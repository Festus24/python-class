
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