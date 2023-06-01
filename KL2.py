# print('1==1', 1==1)#Дорівнює
# print('1==2', 1==2)
# print('1!=1', 1!=1)#Не дорівнює
# print('1!=2', 1!=2)
# print('1>1', 1>1)#Більше ніж
# print('1>2', 1>2)
# print('1<1', 1<1)#Менше ніж
# print('1<2', 1<2)
# print('1<1', 1<1)#Менше ніж
# print('1<2', 1<2)
# print('1>=2', 1>=2)#Менше або дорівнює
# print('1<=2', 1<=2)#Менше або дорівнює

#bool()-перевірка на True False

# print(bool(''))
# print(bool(0.0))
# print(bool(None))
# print(bool('Some Text'))
# print(bool(1))

#and "Логічне множення"
# competent=True
# responsible=True
# print(competent and responsible)
#
# competent=True
# responsible=False
# print(competent and responsible)

#or Логічне додавання
# competent=True
# responsible=False
# print(competent or responsible)
#
# competent=False
# responsible=False
# print(competent or responsible)

#note Логічне заперечення
# previosly_fired=True
# print(not previosly_fired)
#
# previosly_fired=False
# print(not previosly_fired)

# time=int(input('Enter the current time in hours:')) %24
# ticket=False
# money=True
# luggage=False
# print(money or ticket and not luggage and time>6)

# V=int(input('Введить швідкисть '))
# if V>50:
#     print('Машина швbдше 50 км')

# V=100
# if V>50 and V<150:
#     print('Машина між 50 км та 150км')

# v=100
# if 50<v<150:
#     print('Машина між 50 км та 150км')

# a,b,c=int(input('Перше')),int(input('Друге')),int(input('Третє'))
# maximum=a
# if maximum<b:
#     maximum=b
# if maximum<c:
#     maximum=c
# print('Max: ', maximum)

# if 5>4:
#     print('Початок блоку виконання')
#     print('Частина блоку виконання')
#     print('Частина блоку виконання')
#     print('Кінець блоку виконання')
# print('Це не частина блоку виконання')

# car_speed=150
# motorcycle_speed=100
# if car_speed>motorcycle_speed:
#     print('car is faster than motorcycle')
# elif car_speed<motorcycle_speed:
#     print('Motorcycle faster than car ')
# else:
#     print('equally fast')

# number=int(input('Enter the answer number'))
# if number == 1:
#     print('Обрано варіант а')
# elif number ==2:
#     print('Обрано варіант б')
# elif number ==3:
#     print('Обрано варіант в')
# elif number ==4:
#     print('Обрано варіант г')
# else:
#     print('Такого варінту немає')

# myname=input('Введіть логін')
# mypass=input('Введить пароль')
# if myname=='admin' and mypass=='1111':
#     result='Привіт'+myname+', адмін'
# elif myname=='student' and mypass=='qwerty':
#     result='Привіт'+myname+', студент'
# elif myname=='Tatiana' and mypass=='asdasd':
#     result='Привіт'+myname
# else:
#     result='Я тебе не знаю'
# print(result)

# question_1='2+2'
# question_2='3*3'
# question_3='5*5'
# question_4='2+2*2'
# answ_1='4'
# answ_2='9'
# answ_3='25'
# answ_4='6'
# result=0
#
# user_answer=input(question_1)
# if user_answer==answ_1:
#     result+=1
#     print('Correct')
# else:
#     print('Incorrect')
#
# user_answer=input(question_2)
# if user_answer==answ_2:
#     result+=1
#     print('Correct')
# else:
#     print('Incorrect')
# user_answer=input(question_3)
# if user_answer==answ_3:
#     result+=1
#     print('Correct')
# else:
#     print('Incorrect')
# user_answer=input(question_4)
# if user_answer==answ_4:
#     result+=1
#     print('Correct')
# else:
#     print('Incorrect')
#
# print('u have', result, 'points')

print('Введить яку дію виконуємо +,-,*,/.**')
try:
    dia=input('Введить дію')
    a=int(input('Перше число: '))
    b=int(input('Друге число: '))
except:
    print('Вводимо числа')
result=None
if dia == '+':
    result=a+b
elif dia == '-':
    result=a-b
elif dia == '*':
    result=a*b
elif dia == '/':
    try:
        result=a/b
    except:
        print('На нуль ділити не можно')
elif dia == '**':
    result=a**b
else:
    print('Така дія не передбачена')

print(result)

