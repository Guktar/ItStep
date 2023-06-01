# print('Hello')
# print('World')
#
# print('Hello', end='-->')
# print('World')

# print('Hello', 'World', 'hi',sep='-->')

# numbers_1=input('num 1 = ')
# print(type(numbers_1))

number_1=25
number_2=0

#print(number_1/number_2)
# try:
#     number_3
#     print(number_1/number_2)
# except:
#     print('Error')

# try:
#     x=5
#     y='3'
#     print(x**y)
# except:
#     print('Error')

#error='error'
# try:
#     print('start code')
#     print(error)
#     print(5/0)
#     print('no errors')
#
# # except NameError:
# #     print('We have an NameError')
# #
# # except ZeroDivisionError:
# #     print('We have an ZeroDivisionError')
#
# except (NameError, ZeroDivisionError) as error:
#     print(error)
#
# print('\n\t\tcode after capsule')

# try:
#     try:
#         print('start code')
#         print(5/0)
#         print(error_1)
#         print('no errors')
#     except NameError as error:
#         print(error)
# except ZeroDivisionError as error:
#     print(error)

# try:
#     print(Hello)
# except:
#     print('! problems')
# else:
#     print('no problems')
# finally:
#     print('Finally code')

# import tkinter as tk
#
# root=tk.Tk()
# root.title('First Application')
#
# label=tk.Label(root, text='Text',
#                fg='blue',
#                bg='yellow',
#                font=('Arial',20, 'bold italic'))
# label.pack()
# root.mainloop()

# try:
#     try:
#         apples=int(input('Enter the amont of apple you have: '))
#         if apples<0:
#             raise Exception
#             print('You have', apples, 'apples.')
#
#     except Exception:
#         print("You can't have,", apples, "apples")
#
# except:
#     print('bad ...')

# try:
#     raise Exception
# except ValueError:
#     print('Improver value was obtained')
# except Exception:
#     print('....... Something went wrong')

# try:
#     f=open('Some_text.txt')
# except ZeroDivisionError:
#     print('Error 1')
# except:
#     print('Errors ....')

# day=4
# mounth='april'
# year=2023
# print('Today is', day, mounth, year,'.')
# #f Строки
# print(f'Today is {day} {mounth} {year}.')
# print(f'Today is {day:8} {mounth:15} {year:10}.')
# print(f'Today is {day:^8} {mounth:>15} {year:<10}.')
# print(f'Today is {day:^8} {mounth:^15} {year:^10}.')
# print(f'Today is {day:_^8} {mounth:*>15} {year:%<10}.')
# #Метод format()
# print('Today is {} {} {}.'.format(year,mounth,day))
# print('Today is {:%^10.3f} {:*^15} {:_^8}.'.format(year,mounth,day))
# print('Today is {year:%^10.3f} {mounth:*^15} {day:_^8}.'.format(year=2022,
#                                                    mounth='april',
#                                                    day=22))
# print('Today is {year_1:%^10.3f} {mounth_1:*^15} {day_1:_^8}.'.format(year_1=2022,
#                                                    mounth_1='april',
#                                                    day_1=22))
