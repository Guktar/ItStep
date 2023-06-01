# student=['Bob',19,95]# name, age, score
# template="Name:{}; age:{},scores{}"
# users=['admin','teacher','manager']
# while True:
#     print('1-print info')
#     print('2-modify info')
#     print('3-exit')
#     userChoise=input('Select menu item: ')
#     if userChoise=='1':
#         user=input('Login: ')
#         if user in users:
#             print('Current info: ')
#             print(template.format(student[0],
#                                   student[1],
#                                   student[2]))
#     elif userChoise == '2':
#         user = input('Login: ')
#         if user in users:
#             print('Current info: ')
#             print(template.format(student[0],
#                                       student[1],
#                                       student[2]))
#             userAnsw=input('Change this info y-n?')
#             if userAnsw=='y':
#                 name=input('Input new name : ')
#                 age=input('Input new age : ')
#                 scores=input('Input new score : ')
#                 student[0]=name
#                 student[1]=age
#                 student[2]=scores
#                 print(template.format(student[0],
#                                       student[1],
#                                       student[2]))
#     elif userChoise=='3':
#         print('Bye!')
#         break
#     else:
#         print('Wrong menu item')
import math
# help(breakpoint)

#math.ім'я ф-ї(....)
#seil Повертає найближче ціле значення(округлення в гору)
#fllor Повертає найближче значення (округлення вниз)
# import math
# a=0.23
# b=1.87
# c=3
# print(math.ceil(a))
# print(math.ceil(b))
# print(math.ceil(c))
#
#
# print(math.floor(a))
# print(math.floor(b))
# print(math.floor(c))
#
# #modf()-Повертає дробову та цілу частину числа
# x=2.9
# y=1.5
# print(math.modf(x))
# print(math.modf(y))
# #trunc() - Отримання цілої частини числа
# x=2.45
# y=1.5
# print(math.trunc(x))
# print(math.trunc(y))
# #abs - повертає модуль числа з таким самим типом як і вихідне число
# #fabs - повертає модуль числа з типом float
# q=-2
# w=-2.5
# e=4
# print(math.fabs(q))
# print(math.fabs(w))
# print(math.fabs(e))
#
# print(abs(q))
# print(abs(w))
# print(abs(e))
#
# #factorial - факторіал 4!=4*3*2*1=24 Завжди якщо число не ціле то Vallue error або TypeError
# p = 4
# e = 7.4
# try:
#     print(math.factorial(p))
#     print(math.factorial(e))
# except TypeError:
#     print('Not correct item')


#randint(a,b) - Приймає лише два аргумента і саме з цього діапазону-випадкове числоперше
#має бути завжди менше другого


# import random
# for i in range(3):
#     print('Step', i+1)
#     print(random.randint(1,5))
#     print(random.randint(-3,20))
#     print(random.randint(-10,-6))
#randrange() - Від 1 до 3-х аргументів
#randrange(a) - Випадкове число від 0 до вказаного[0:a) від 0 до а-1
#randrange(a,b) - аналогічно до randint але верхнє число не входить до діапазону [a:b) від a до b-1
#randrange(a,b,c)- Перші два числа є межами діпазону, третє це крок генератора. (10,18,2) 10,12,14,16

# import random
# for i in range(3):
#     print('Step', i+1)
#     print(random.randrange(10))
#     print(random.randrange(-4,3))
#     print(random.randrange(10,20,3)) # 10,13,16,19

#random - Виклик без аргументів, випадкове число генерується в діапазоне від 0 до 1 але не включаючи 1
# import random
# for i in range(3):
#     print('Step',i+1)
#     print(random.random())

#choise(l)  - l-це послідовність або її ім'я Ф-я для отримання випадкового елемнту з послідовності
# import random
# L=[1,23,'Bob',True,False,7.9,'hello']
# for i in range(3):
#     print(random.choice(L))
#     print(random.choice(['red','blue','green','white']))

# import random
# import math
#
# while True:
#     dia=int(input('Оберить одну із дій'
#                   '\n 1 - Визначити Факторіал'
#                   '\n 2 - Надати абсолютне значення'
#                   '\n 3 - Згенерувати число від 1 до 100'
#                   '\n 4 - Згенерувати число з діпазону'
#                   '\n 5- Quit'
#                   '\nОберить Одну із дій : ')
#             )
#     if dia == 1:
#         a=int(input("Введить число факторіал котрого хочете отримати : "))
#         print('Ваш факторіал', math.factorial(a))
#     elif dia==2:
#         a=float(input("Введить число: "))
#         print('Ваше абсолютне значення : ', math.fabs(a))
#     elif dia==3:
#         for i in range (1):
#             print('Ваше число', random.randrange(1,100))
#     elif dia==4:
#         a=int(input('Введить перше значення діапазону '))
#         b=int(input('Введить друге значення діапазону '))
#         print(random.randrange(a,b))
#     elif dia==5:
#         break
#     else:
#         print('Вибрано не вірна дія')


#def ім'я(): починається завжди з літери або нижнього _ містить лише букви, цифри і _

# def printMsg():
#     print('Hello')
#     print('Welcome')
# printMsg()
# print('Bye')

# def printMsg1(myMsg):
#     print(myMsg)
#
# def printMsg2(myMsg1,myMsg2):
#     print(myMsg1)
#     print(myMsg2)
#
# myMsg1='Hello'
# myMsg2='World'
# printMsg2(myMsg1,myMsg2)

# def calculate(a,b,c):
#     print('lets calculate')
#     print(a+b*c**2)
#
# q=5
# w=2
# e=3
# calculate(q,w,e)
# calculate(q,w,3)
# calculate(5,2,3)
# def modifyName(userName):
#     newName=userName.upper()
#     return newName
# name=input('input your name : ')
# print(modifyName(name))
# print(f'User name : {modifyName(name)}')
# a=modifyName(name)
# b=a+', Hello user'
# print(b)
# def calculate(a,b):
#     return a+b
#
# a=float(input('Input a: '))
# b=float(input('Input b: '))
# if calculate(a,b)<=0:
#     y=5*a+2*b
# else:
#     y=10*a-3*b
#
# print(f'Y = {y}')

# def checkCustomer(customer,customers):
#     result=0
#     print('Clients positions in the list: ')
#     for i in range(len(customers)):
#         if customers[i]==customer:
#             print(i)
#             result+=1
#     return result
#
# customerList=['Bob','Anna','Joe','Bob','Nick']
# myCustomer=input('Enter name : ')
#
# if checkCustomer(myCustomer,customerList)>1:
#     print(f'Customer {myCustomer}, will get a discount')

# def modifyName2(userName):
#     newName1=userName.upper()
#     newName2=userName.lower()
#     return newName1, newName2
#
# name=input('Enter your Name: ')
# print(modifyName2(name))
# nameUpper, nameLower=modifyName2(name)
# print(nameUpper)
# print(nameLower)

# def checkLog(userLog):
#     if userLog.lower()=='admin':
#         return userLog.upper()
#     elif userLog.lower()=='user':
#         return userLog.lower()
#     else:
#         return 'Wrong login'
#
# login = input('Enter your login: ')
# print(checkLog(login))

# def meanF(*args):
#     s=0
#     k=0
#     for i in args:
#         s+=i
#         k+=1
#     return s/k
#
# print('(1+5+7)/3=', meanF(1,5,7))
# print('(1+5+7+4+9+12+13)/7=', meanF(1,5,7,4,9,12,13))

# def userGreatings(login,passw='1111'):
#     if login=='admin':
#         print('Welcome, admin')
#         print(passw)
#     elif login=='student':
#         print('Welcome, student')
#     else:
#         print('Welcome. IDK who are u')
# userGreatings('admin')
# userGreatings('admin','qwerty')

#
# def a(a,b,c):
#     print(a,b,c)
#
# a(1,2,3)  #Позиційні аргументи


# def calcBMI(m,h):
#     return m/(h**2)
#
# print(calcBMI(h=1.6,m=50)) #Іменовані
# print(calcBMI(50,1.6)) #Позиційні










