# Lists and tuple
"""
List
"""
#     Creating and accessing elements
#     List methods (append, extend, insert, remove)
#     List comprehensions
#     Tuples and immutability
#     Choosing between lists and tuples
#     Nested data structures

#   Creating and accessing elements
# list1 = []
# list2 = list(())
student_name = ["Oba", "Festus", "Emmanuel", "Kenny", "Ibrahim", "Samuel"]
# print(student_name)
# student_name.append("Tife")
# student_name.insert(2, "Tife")
# student_name.remove("Samuel")
# student_name.extend("Oba")
# student_name.reverse()
# x = student_name.__add__(["Aliyu"])

# new_student = ["Temiloluwa", "Gafar", "Nurudeen"]
# student_combo = student_name.__add__(new_student)
# print(student_combo)

# for new in new_student:
#     student_name.append(name)
# print(student_name)

# student_name[2] = "Zion"
# print(student_name)

# List comprehensions
# for i in range(1, 10):
#     print(i)
# list_nmm = [i for i in range(1, 10)]
# print(list_nmm)

# list_student = [name for name in student_name if len(name) <=6]
# print(list_student)

# list_num = [5, 4, 10, 25, 15, 27, 60, 100]
# even_num = [n for n in list_num if n%2==0]
# print(even_num)

# Nested dara structures
# student_record = [["Oba", "Cyber", 20265], ["Festus", "Native app", 20266], ["Kenny", "Network appl", 20266]]
# print(student_record[1][0])

# for container in student_record:
#     print(container)

# for name, deoartment, matric_no in student_record:
#     print(name, matric_no)

# student_record[2][1] = "Fishery"
# print(student_record)