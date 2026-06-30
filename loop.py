"""
Loop
"""
# for loops and range()
# for i in range(10):
#     print(i)

# for i in range(1, 100, 2):
#     print(i)

fruits = ["Banana", "Apple", "Orange", "Cherry", "Mango"]
# for x in fruits:
#     print(x)

# for x in range(len(fruits)):
#     print(x)

# for fruit in fruits:
#     print(fruit.upper())

# fruits_name = []
# for l in fruits:
#     if l in ["Apple", "Mango"]:
#         fruits_name.append(l.upper())

#     else:
#         fruits_name.append(l)
# print(fruits_name)

# Loop control statements (breaks, continue)
# for num in range(20):
#     if num == 15:
#         break
#     print(num)

# for num in range(20):
#     if num == 10:
#         continue
#     print(num)

# for name in fruits:
#     if name == "Cherry":
#         break
#     print(name)

# for name in fruits:
#     if name == "Apple":
#         continue
#     print(name)

# for size in fruits:
#     print(len(size))

# for r in range(12):
#     for k in range(12):
#         print(r,k)

# fruits = ["Banana", "Apple", "Orange", "Cherry", "Mango"]
# for n in fruits:
#     for x in n:
#         print(n,x)

# while loops
# infint loop
# a = 0
# count = 0
# while a<10:
#     count +=1
    # print(a, count) 

# x = 0 
# while x<=10:
#     print(x)
#     x+=1

# x = 10
# while x>0:
#     print(x)
#     x-=1

# num = 0
# while num <20:
#     num+=1
#     if num == 11:
#         break
#     print(num)

num = 0
while num <20:
    num+=1
    if num == 11:
        continue
    print(num)