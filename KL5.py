# myStr='hello'
# print(id(myStr))
# print(type(myStr))
# print(myStr)
# zminna_ryadok='''hello 1
#                 hello 2
# hello 3'''
# print(zminna_ryadok)

# a='Python'
# print(a[0])
# print(a[1])
# print(a[-1])
# print(a[len(a)-1])

# a='Hello'
# b='World'
# print(a+b)
# print(a*5)

# a='встречаются В русском языке встречаются названия пито́н[23] или па́йтон[24]) — высокоуровневый язык программирования общего назначения с динамической строгой Типизацией и автоматическим управлением памятью[25][26], встречаютсяориентированный На повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ[27].'
# print(a.capitalize()) #Перший символ - верхній регістр, інші у нижній
# print(a.lower()) #усе переводиться у нижній регістр
# print(a.upper()) #усе переводиться у верхній регістр
# print(a.title()) #Перші літери слів у верхній регістр, а інші в нижній
# print(a.swapcase()) #Змінює регістр на протилежний
#
# print(a.count('встречаются')) #К-ть входжень фрагмента до рядка
# print(a.count('встречаются',20,65)) #К-ть входжень фрагмента до рядка з 20 до 65 символу
# print(a.count('встречаются', 20)) #К-ть входжень фрагмента до рядка з 20 до кінця
#
# print(a.find('названия')) #Індекс першого входження
# print(a.find('встречаются', 20))
# print(a.find('встречаются', 20,65))
#
# print(a.index('встречаются'))#Індекс першого входження, якщо нема ValueError
# try:
#     print(a.index('встречаются',40,65))
# except ValueError:
#     print('Даний фрагмент не було знайдено')
# finally:
#     print('Дякуємо, що скористалися нашим пошуком')
#
# print(a.rfind('встречаются')) #Індекс останнього входження
# print(a.rfind('встречаются',20,65))
#
# print(a.rindex('встречаются'))#Індекс останнього входження, якщо нема ValueError

# slovo=input('Введить слово: ')
# rech="Розробка мови Python була розпочата в кінці 1980-х років[9] співробітником голландського інституту CWI Гвідо ван Россумом. Для розподіленої ОС Amoeba потрібна була розширювана скриптова мова, і Гвідо почав писати Python на дозвіллі, запозичивши деякі напрацювання для мови ABC (Гвідо брав участь у розробці цієї мови, орієнтованої на навчання програмування). У лютому 1991 року Гвідо опублікував вихідний текст в групі новин alt.sources[10]. Мова почала вільно поширюватися через Інтернет і сподобалася іншим програмістам. З 1991 року Python є цілком об'єктно-орієнтованим. Python також запозичив багато рис таких мов, як C, C++, Modula-3[en] і Icon[en], й окремі риси функціонального програмування з Ліспу."
# try:
#     print(f'Таке слово знайдено  {rech.index(slovo)}')
# except ValueError:
#     print("Такого слова нема")

# zminna="python (найчастіше вживане прочитання — «Па́йтон», запозичено назву[7] з британського шоу Монті Пайтон) — інтерпретована об'єктно-орієнтована мова програмування високого рівня зі строгою динамічною типізацією.[8] Розроблена в 1990 році Гвідо ван Россумом."
# print(zminna.startswith('p')) #Чи починається рядок з заданого фрагмента
# print(zminna.startswith('P'))
# print(zminna.startswith('python'))
# print(zminna.startswith('p',90))
#
# print(zminna.endswith('.'))#Чи закінчується рядок на заданий фрагмент
# print(zminna.endswith('n',0,6))
# print(zminna.endswith('.',0,6))

# stroka='Python2023'
# print(stroka.isalnum())#Перевіря чи рядок складається з літер і чисел
# print(stroka.isalpha())#Перевіря чи рядок складається лише з літер
# print(stroka.isdigit())#Перевіря чи рядок складається лише з чисел

# a=input('Enter 1 number ')
# b=input('Enter 2 number ')
# if a.isdigit()==True and b.isdigit()==True:
#     c=int(a)+int(b)
#     print(c)
# else:
#     print('Ви ввели некоретне значення')

# stroka='hello'
# print(stroka.islower())#Перевіряє чи всі елементи рядка у нижньому регістрі
# print(stroka.istitle())#Перевіряє чи кожне слово рядка починається з великої літери
# print(stroka.isupper())#Перевіряє чи всі елементи рядка у верхньому регістрі
#
# stroka_1='\n\t\n    \n'
# print(stroka_1.isspace())#Лише пробілові символи - пробіл, табуляція, перехід на новий рядко

# stroka='Pyt\thon'
# print(stroka.center(30))
# print(stroka.center(30,'*'))
# print(stroka.center(50,'-'))
# print(stroka.expandtabs(tabsize=8))#Задаємо скільки пробілів \t
# print(stroka.ljust(30,'@'))
# print(stroka.rjust(30,'0'))

# stroka='Python-cool!'
# print(stroka[1:3])
# print(stroka[-5:-2])
# print(stroka[-5:11])
# print(stroka[:])
# print(stroka[-5:])
# print(stroka[7:])
# stroka_1='0123456789'
# print(stroka_1[2:8:2])
# print(stroka_1[9:2:-2])
# print(stroka_1[::-1])
# print(stroka_1[5::2])
# print(stroka_1[-1::-2])
# print(stroka_1[:len(stroka_1):3])

# a=r'\n-new line'
# print(a)
# b=R'\t\tAddition+\n'
# print(b)
# c=r'\ '
# print(c)
# d=r'abc\\'
# print(d)
# zminna="python (найчастіше вживане прочитання — «Па́йтон»," \
#        " запозичено назву[7] з британського шоу Монті Пайтон)" \
#        " — інтерпретована об'єктно-орієнтована мова програмування " \
#        "високого рівня зі строгою динамічною типізацією.[8] " \
#        "Розроблена в 1990 році Гвідо ван Россумом."
# day=11
# mounth='Квітень'
# year=2023
# print('Todday {}.{}.{} '.format(day,mounth,year))
# print('Todday {day}.{mounth}.{year}'.format(mounth=mounth, day=11, year=2023))
# print(f'Todday {day} {mounth} {year}')

# name='Tatiana'
# year=2023
# print(f'Hello {name}')
# print(f'Hello {name*2}')
# print(f'Hello {len(name)}, Now is {year}')
# print(f'Hello {name}, Now is {year}')
# print(f'Hello {name:-^30}, Now is {year}')
# print(f'Hello {name:-<30}, Now is {year}')
# print(f'Hello {name:->30}, Now is {year}')
# #^-вирівнювання по центру
# #<-Вирівнювання за лівим краєм
# #>-Вирівнювання за правим краєм

a,b,c,d=map(int,input().split())
dob=a*b*c*d
print(dob)








