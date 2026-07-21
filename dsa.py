# Stack and Queue
# Creating a stack and queue
# stack operations(push, pop, peak,isEmpty, size)
# Queue basic operations (Enqueue, Dequeue, popleft, peek isEmpty, size)
# Link Lists, Hash table

# from collections import deque
# class Queue:
#     def __init__(self):
#         self.queue_container = deque()
    
    # Enqueue
#     def Enqueue(self, value):
#         self.queue_container.append(value)
    
#     # Dequeue
#     def Dequeue(self):
#         c = self.queue_container.popleft()
#         return c

# Q1 = Queue()

# Q1.Enqueue(20)
# Q1.Enqueue(True)
# Q1.Enqueue("Apple")
# Q1.Enqueue(30.0)

# print("Dequeu: ", Q1.Dequeue)
# print(Q1.queue_container)

# hash Table
# student_record = {
#     "01":["Oba", 202620, "cyber security"],
#     "01":["Fatimah", 202621, "Data science"]    
# }
# print(hash(tuple(student_record["01"]))),student_record["01"]

student_info = {"name":"Oba", "department":"cyber", "matric_no": 202567}
print(hash(student_info["name"]))
print(hash(student_info["department"]))
print(hash(student_info["matric_no"]))











# class stack:
#     def __init__(self):
#         self.stack_list = []
        
#         # Push
        
#     def Push(self, fruit):
#         self.stack_list.append(fruit)
#         # return self.stack_list
    
#     def Pop_list(self):
#         k = self.stack_list.pop()
#         return k
    
#     def Peek(self):
#         return self.stack_list[-1]
    
#     def isEmpty(self):
#         if len(self.stack_list)==0:
#             return "container is empty"
        
#         else:
#             return "Not Empty"
    
#     def size(self):
#         x=len(self.stack_list)
#         return x
    
# p1 = stack()

# p1.Push("Apple")
# p1.Push("Banana")
# p1.Push("Orange")

# print("pop: ", p1.Pop_list())
# print("Peek: ", p1.Peek())
# print("isEmpty: ", p1.isEmpty())
# print("size: ", p1.size())
# print(p1.stack_list)