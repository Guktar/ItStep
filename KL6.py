# a='test It step Text'
# print(a)
# print(a.center(60))
# print(a.strip())

# a=[12,12,11,12,11,10]
# student=['Alex','Marc','Katy']
# t=[10.2,10.5,10.3]
# test=[12,12,'Text']
# print(a)
# print(student)
# print(test)

# 1) create
# student=['Alex','Marc','Katy','Tanya']
        # 0        1      2     3        - index
# 2) read
# print(student)
# print('Hi' , student[0])
# print('Hi' , student[0], student[1])
# print(student[1:3])
# print('Hi' , student[1])
# print('Hi' , student[2])
# print('Hi' , student[3])
# a=[12,12,11,12,11,10]

# print(a[2])

# 3) append
# a=[12,12,11,12,11,10]
# print(a)
#
# # a.append(9) Тільки одну позицію
# a.extend(
#     [1,2,3]
# ) #Можно додати декілька елементів
# print(a)
# a.insert(2,9)
# print(a)
# 4) remove
# student=['Alex','Marc','Katy','Tanya']
# print(student)
#
# i=student.index('Katy')
# print(i,student[2])
# # del(student[2])
# del(student[i])
# print(student)

# 5) edit

# student=[12,11,10,9]
#         # 0  1  2  3
#         #-4 -3 -2 -1
# print(student)
# student[3]=12
# student[1]=12
# student[-2]=12
# print(student)
#CRUD - create read update delet

# student=['Alex','Marc','Katy','Tanya']
#
# student.append('Bob')
#
# for item in student:
#     print('Hi',item)
#     if student[i]=="Alex":
#         student[i]='Alex2'
#     print(student)
#     print(item, [10,11,12])
# print(student)
# for i in range(len(student)):
#     print(i, student[i])
#     if student[i]=="Alex":
#         student[i]='Alex2'
# print(student)
# a=[1,2,3,4]
#
# b=[5,6,7]
#
# print(a)
# print(b)
# c=a+b
# print(c)
# #1
# auto=['Ford', 'Tesla', 'Volkswagen', 'Mercedes']
# models=['Mondeo','Model X', 'Polo', 'Benz']
# #2
# print(auto[1])
# #3
# models[-1]='GLC'
# print(models)
# #або
# for i in range(len(models)):
#     print(i, models[i])
#     if models[i]=='Benz':
#         models[i]='Glc'
# print(models)
# #4
# auto_models=auto+models
# print(auto_models)

# b=[
#     #  0       1
#     ['Artem', "Mark"], #0
#     # 0        1      2
#     ["katy", "Alex",'Artem'],#1
# ]
# # b=['Artem','Mark']
# print(b[1][2])
# print(b[0][1])

# a=[1,2,3,4]
# b=[5,6,7]
# c=[8,9,10]
#
# d=a+b+c
# print(a)
# print(b)
# print(c)
# print(d)

# a=[0]*100
# # print(a)

# a=[[12,12,12]]+[[0,0,0,0]]*100
# print(a)

# a=['It', 'st', 'ap']
# print(a)
#
# a[0:2]=['IT','ST', 11]
# print(a)

# a=[1,2,3,4,5]
# l=[6,7,8,9]
# a.extend(l)
# print(a)
# print(a)
# a.append(6)
# print(a)

# a=[1,2,3,4,5]
# a.insert(3,4)
# print(a)

# a=[1,2,3,4,5,4,3,2,4,5]
# a.remove(4)
# a.remove(4)
# print(a)

# a=[1,2,3,5,8,13,21]
# val=a.pop(5)
# print(a)
# print('Видалeно елемент', val)

# a=[1,2,3,5,8,13,21,13,14,44,55]
# i=a.index(13)
# print(i)
# i=a.index(13,6)
# print(i)
# i=a.index(13,6,-3)
# print(i)
# print(a[i])
# a=[1,2,3,5,8,13,21,13,14,44,55,4,2,3,4,5,6]
# print(a.count(13))
# print(a.count(0))
# print(a.count(2))

# a=[1,2,3,5,8,13,21,13,14,44,55,4,2,3,4,5,6]
# # print(0 in a)
# if 0 in a:
#     i=a.remove(4)
# print(a)

# a=[4,346,45,8,9,43,3,6]
# print(a)
#
# a.sort()
# print(a)
#
# a.sort(reverse=True)
# print(a)
# print(a[1])

# a=['Mark','Roman',"Andrii",'Alex']
# print(a)
# a.sort()
# print(a)

# a=['Mark','Roman',"Andrii",'Alex']
# print(a)
# a.reverse()
# print(a)

# students_ALL=[[]]
# students=['Mark','Roman',"Andrii",'Alex']
# print(students)
# students.clear()
# print(students)
# students=['Bob']
# print(students)

# students=[9,10,11,6,12,5]
# # print(len(students))
# # print(max(students))
# # print(min(students))
# # print(sum(students))
# # print(sum(students)/len(students))
# b=sorted(students,reverse=True)
# print(sorted(students))
# print(b)

# a=[12,12,11,9,13]
# b=a.copy()
# # a[0]=11
# print(a)
# print(b)
# a[0]=1
# print(a)
# print(b)




















