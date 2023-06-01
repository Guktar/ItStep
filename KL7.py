# userTypes=['admin','student','teacher']
# userTypes[0]='user'

# a=(1,2,3,[1,2])
# a[3][1]=3
# print(a)

# myTuple=()
# myTuple1=tuple()
# print(myTuple)
# print(type(myTuple))
# print(myTuple1)
# print(type(myTuple1))

# myTuple1=('element',12,36.6,False)
# myTuple2=('item1',)
# myTuple3='admin','student','teacher'
# myTuple4='Name',
#
# print('myTuple1:', myTuple1, 'type', type(myTuple1))
# print('myTuple2:', myTuple2, 'type', type(myTuple2))
# print('myTuple3:', myTuple3, 'type', type(myTuple3))
# print('myTuple4:', myTuple4, 'type', type(myTuple4))

# itemTuple=(1,2,1,2)
# print(itemTuple)

# namesTuple1=tuple(('Hi', 'Buy'))
# namesTuple2=tuple(('Hello', 'Good'))
# print(namesTuple1)
# print(namesTuple2)

# users=('admin','student','hr','moderator')
# print('1stuser',users[0])
# print('last user',users[len(users)-1])
# print('last user one more time user',users[-1])
# print('1st two users:', users[:2])
# print('2nd and 3rd users:', users[1:3])
# # users[0]='user'
# del users
# print(users)

# danni=('Mon','Tue','Wed','Thu')
# day1,day2,day3,day4=danni
# print(day1)
# print(day2)
# print(day3)
# print(day4)

# danni1=("Python",'Java','C++','C#')
# mova, *movi=danni1
# print(mova)
# print(movi)

# cifri=(1,2,3,4)
# num, *nums, num2=cifri
# print(num)
# print(nums)
# print(num2)

# cart=(True,False,'some info',4)
# for danni in cart:
#     print(danni)
# for i in range(len(cart)):
#     print(cart[i])

# A=(1,2,3)
# B=(4,5,6)
# C=A+B
# print(C)
#
# D=(3,'stroka')+(-26.5,['spysok',False])
# print(D)
#
# N=('str','stroka')
# S=N+(5,6)+(True,False)
# print(S)

# cort=(1,2,3)*3
# print(cort)
#
# cort1=('stroka','Hello','World')
# for i in cort1*4:
#     print(i)

# myTuple1=("Python",'Java','C++','C#','Python')
# print(myTuple1.count('Python'))
# print(myTuple1.index('Java'))
# if 'C++' in myTuple1:
#     print('Yes')

# while True:
#     firstName = input('Input your first name: ')
#     lastName = input('Input your last name: ')
#     yearBirth = input('Input your Birth year: ')
#     gender = input('Inpit your gender (M,F): ')
#     if firstName == '' or lastName == '' or yearBirth == '' or gender not in ('F', 'M'):
#         print("Wrong data")
#     else:
#         info = (firstName, lastName, yearBirth, gender)
#         print(info)
#
#     hobbyInd = 1
#     hobbyList = []
#
#     while True:
#         hobbyName = input('Name of the hobby #{}:'.format(hobbyInd))
#         if hobbyName == '':
#             print("No info")
#             break
#         else:
#             hobbyList.append(hobbyName)
#             hobbyInd+=1
#
#     if len(hobbyList)>0:
#         print(f'You have {hobbyInd-1} hobbies')
#     else:
#         print('You dont have hobbies')
#
#     progId=1
#     infoprog=[]
#     while True:
#         prog=input(f'Name of prog lang {progId} ')
#         if prog=='':
#             print('U didnt enter info')
#             break
#         else:
#             infoprog.append(prog)
#             progId+=1
#
#     if len(infoprog)>0:
#         print(f'You know {progId-1} prog lang')
#     else:
#         print('You dont know progging')


# fruits = ("apple", "banana", "orange", "mango, pineapple","banana-mango", "banana-apple")
# fruit = input("Input a fruit:")
#
# for f in fruits:
#     if f in fruits:
#      count += f.count(fruit)
#
# print("There are '{}' in tapple: {}".format(fruit, count))

"""Множини"""

# mySet1={1,2,3}
# mySet2={'Joe','Bob',"Kate"}
# mySet3={'Bob',23,False,(45.6,12)}
# print(mySet1)
# print(mySet2)
# print(mySet3)
# mySet4=set((10,20,30,))
# print(mySet4)

# a={'Joe','Joe','Bob','Kate'}
# print(a)
# spysok=['Joe','Joe','Bob','Kate']
# new_mnoj=set(spysok)
# print(new_mnoj)
# print(list(new_mnoj))

# A={1,2,3}
# B={3,2,1}
# print(A==B)

# userNames={'Joe','Bob','Kate'}
# for name in userNames:
#     print(name)

# userNames={'Joe','Bob','Kate'}
# name=input('Your name: ')
# if name in userNames:
#     print(f'Welcome, {name}, admin')

# mySet={1,2,3}
# print(mySet)
# mySet.add(4)
# print(mySet)
# mySet.update([3,4,5])
# print(mySet)
# mySet.update([5,6,7],{8,9})
# print(mySet)
# mySet.discard(9)
# print(mySet)
# mySet.discard(10)
# print(mySet)
# # mySet.remove(10)

# studGroup={'Hanna','Joe','Kate'}
# studGroup2={'Bob','Joe','Jane','Jake'}
# print(studGroup)
# print(studGroup2)
#
# print('Перетин множин')
# print(studGroup&studGroup2)
# print(studGroup.intersection(studGroup2))
#
# print("Об'єднання")
# print(studGroup|studGroup2)
# print(studGroup.union(studGroup2))
#
# print('Різниця')
# print(studGroup2-studGroup)
# print(studGroup2.difference(studGroup))

# allPizzaTypes=[]
# while True:
#     a=input('Do you want to enter new pizza?')
#     if a=='y':
#         b=input('pizza')
#         allPizzaTypes.append(b)
#     elif a=='n':
#         break
#     else:
#         print('Not correct info')
#
# pizza_unique=list(set(allPizzaTypes))
# print(pizza_unique)

# userApp1=['user134','admin56','superBob','student','spider34']
# userApp2=['fifa56','user134','studGood','admin56','spider34']
# userApp3=['hello','world']
#
# print('Користувачі двох додатків')
# print(set(userApp1)&set(userApp2))
#
# print('Користувачі тільки першого додатку')
# print(set(userApp1)-set(userApp2))
# print('Користувачі тільки другого додатку')
# print(set(userApp2)-set(userApp1))
#
# print("Усі користувачі")
# print(set(userApp1)|set(userApp2))
#
#
# print(set(userApp2)&set(userApp3))

# word1=(input('1st word: '))
# word2=(input('2nd word: '))
#
# if set(word1)==set(word2):
#     print('Yes')
# else:
#     print('No')

# spysok=[1,2,2]
# cort=tuple(spysok)
# print(cort)
sp=[]
import random

i=0
while i<5:
    d=random.randrange(0,20)
    sp.append(d)
    i+=1
print(sp)






