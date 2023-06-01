# number=int(input('Введить число - (до 10) : '))
#
# while number<10:
#     print(f'number = {number}')
#     number+=1.5
#
# print('Цикл завершено')
#
# print('___________')
# number=float(input('Введить число - (до 10) : '))
# while True:
#     print(f'number = {number}')
#     number+=1.5
#     if number >=10:
#         break
#
#     str=input("Бажаєте продовжувати - ")
#     if str=='no' or str=='N:':
#         break

# import random
# #from random import randint
# print('Гра - Вгадай число!')
# bot_number=random.randint(1,10)
# #bot_number=randint(1,10)
# num_2=0
# while True:
#     num_2+=1
#     user_number=int(input('Введить число /до 10/ - '))
#     if user_number>bot_number:
#         print('Ваше число більше ніж бота')
#     elif user_number<bot_number:
#         print('Ваше число менш ніж бота')
#     elif user_number==bot_number:
#         print(f'\nГру закинчено\nЧисло було {bot_number}'
#               f'\nВи вгадали з {num_2} спроби')
#         break
#     if num_2>2:
#         print(f'\nЗагадане число було {bot_number}'
#               f'\nВи не вгадали')
#         break

# import random
# bot_number=random.randint(1,10)
# user_number=0
# while True:
#
#     while bot_number!=user_number:
#         user_number=int(input('Введить число /до 10/ - '))
#         if user_number > bot_number:
#             print('Ваше число більше ніж бота')
#         elif user_number < bot_number:
#             print('Ваше число менш ніж бота')
#         elif user_number == bot_number:
#             print(f'\nГру закинчено\nЧисло було {bot_number}')
#
#     str=input('Бажаєте продовжити Y/N - ')
#     if str=="y" or str == 'Y':
#         bot_number=random.randint(1,10)
#     else:
#         break
#
# print('\nГру завершено')
# while ...:
#
# else:
#     break

# import random
# bot_number=random.randint(1,10)
# user_number=0
# while True:
#
#     while True:
#         user_number=int(input('Введить число /до 10/ - '))
#         if user_number > bot_number:
#             print('Ваше число більше ніж бота')
#         elif user_number < bot_number:
#             print('Ваше число менш ніж бота')
#         elif user_number == bot_number:
#             print(f'\nГру закинчено\nЧисло було {bot_number}')
#             break
#
#     str=input('Бажаєте продовжити Y/N - ')
#     if str=="y" or str == 'Y':
#         bot_number=random.randint(1,10)
#     else:
#         break
#
# print('\nГру завершено')

# number=input('Введить ціле число ')
# while type(number) != int:
#     try:
#         number=int(number)
#     except ValueError:
#         print('Не вірно ввели число ....')
#         number=input('Введить ціле число ')
# print('OK!')

# print('5+5**2=', eval('5+5**2'))

#for-цикл

# x=5
#
# for i in 2,3,4:
#     x+=i
#     print(f'{i} ---> x = {x}')

# x=5
# for i in range(5): #i --> 0,1,2,3,4
#     x+=i
#     print(f'{i} ---> x = {x}')

# for i in range(1,11):
#     print(f'i --> {i}')

# for i in range(1,11, 2):
#     print(f'i --> {i}')

# for i in range(1,11,3):
#     print('i ---->', i,  end='')
#     if i%2==0:
#         print('Парне\n')
#     else:
#         print('Не парне\n')
#     # print('\n ')

# str='strings'
# # print(len(str))
# # print(str[0])
# # print(str[-7])
# x=0
# for i in range(len(str)):  #for i in range(7):
#    print(str[i])
#
# lst=[27,'mama',['papa', 56], 67]
# for i in lst:
#     print(i)
# print(lst[2][0])

# str=input('Enter some string - ')
# for i in str:
#     print(str)
#
# line=input('Enter some string - ')
# for c in line:
#     print(c)

# str='mamapapa'
# print(str[0:4])
# print(str[:4])
# print(str[:4:2])
#
# line=input('Enter some string - ')
# for c in line[::2]:
#     print(c)
#
# for i in range(1,10):
#     for j in range(1,10):
#         print(f'i*j= {i*j}', end='\t')
#     print('\n')
#
# floor=1
# energy=20
# while floor!=5:
#     print('floor before - ', floor )
#     step=0
#     while step!=20:
#         step+=1 # step=step+1
#         energy-=1
#         if energy == 0:
#             print('Відпочивати треба!')
#             energy+=20
#     floor+=1
#     print('floor after - ', floor)
#
# print('floor = 5')