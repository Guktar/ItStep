#datetime(year,month,day, hour=0,minute=0,second=0,microsecond=0)
# import datetime

# dates=datetime.datetime(2023,5,23,hour=19, minute=25, second=53, microsecond=585)
# print(f'object datetime - {dates}')
# print(f'type - {type(dates)}')

# dates=datetime.datetime(2023,5,23,hour=19, minute=25, second=53, microsecond=585)
# print(f'method data() - {dates.date()} type of its result - {type(dates.date())}')
# print(f'method time() - {dates.time()}, type of its result - {type(dates.time())}')
# date1=datetime.date(2021,9,24)
# time1=datetime.time(5,8,48)
# print(f'date = {date1}')
# print(f'time = {time1}')
# date_and_time=datetime.datetime.combine(date1,time1)
# print(f'datetime = {date_and_time}, type date = {type(date_and_time)}')
# print(f'new date = {date1.replace(2022)}')
# print(f'old date = {date1}')
#
# import datetime
#
# date_now=datetime.datetime.now()
# date_today=datetime.datetime.today()
# date_date=datetime.date.today()
# #date_time=datetime.time.now()
# print(f'data now = {date_now}')
# print(f'data today = {date_today}')
# print(f'data today without time = {date_date}')
#
# print(f'time now = {date_now.time()}')
#
# #weekday
# #isoweekday
# date_for_now=datetime.datetime.now()
# print(f'weekday() = {date_for_now.weekday()}')
# print(f'isoweekday() = {date_for_now.isoweekday()}')

#%A- повна назва дня тижня
#%B - повна назва місяця
#%d - день місяця [01,31]
#%H - Година(24-годиний формат)
#%m - номер місяця
#%M - число хвилин
#%S - число секунд
#%x - дата
#%X - час
#%Y - рік

# import datetime
#
# date_now=datetime.datetime.now()
# print(f'date time to str = {date_now.strftime("%d.%m.%Y %H:%M:%S %A %B %U")}')
#
# date_str='28/09/2021 11:20'
# date_str_res=datetime.datetime.strptime(date_str,'%d/%m/%Y %H:%M')
# print(f'str to datetime = {date_str_res}')

# import datetime
#
# date_now=datetime.datetime.now()
# date=datetime.datetime(day=20, month=8, year=2020)
# print(date_now-date)

# import datetime
#
# date_now=datetime.datetime.now()
# print(f'date now = {date_now}')
# delta=datetime.timedelta(days=20,hours=8,weeks=4)
# print(f'delta = {delta}')
# print(date_now+delta)
# a=date_now+delta
# print(f'future date = {a.strftime("%d.%m.%Y %H:%M:%S")}')

# import datetime
#
# while True:
#     data_now=datetime.datetime.now()
#     dia=int(input('1 - Дізнатися день тижня'
#                   '\n2 - Дізнатися яка година'
#                   '\n3 - Розрахувати к-ть днів до наступної дати'
#                   '\n4 - Розрахувати який день буде через к-ть днів'
#                   '\n5 - Вийти'
#                   '\nОберить вашу дію : '))
#     if dia==1:
#         print(f'Сьогодні --> {data_now.strftime("%A")}')
#     elif dia==2:
#         print(f'Зараз --> {data_now.strftime("%H:%M:%S")}')
#     elif dia==3:
#         data_future=input('Введить дату : ')
#         date = datetime.datetime.strptime(data_future, '%d.m$.$Y')
#         data_res=date-data_now
#         print(f'До наступної дати - {data_res}')
#     elif dia==4:
#         data_future=int(input('Введить к-ть днів: '))
#         delta = datetime.timedelta(data_future)
#         print(f'Через {data_future} днів  буде {data_now+delta}')
#     elif dia==5:
#         break
#     else:
#         print('Inccorrect')

# import os
#
# path=os.path.normpath('C:\Windows\Web')
# for path,dirnames,filenames in os.walk(path):
#     print(f'path - {path}')
#     print(f'dirnames - {dirnames}')
#     print(f'filenames - {filenames}')

# import os
#
# path=os.path.normpath('new_dir')
# os.mkdir(path)

# import os
#
# path=os.path.normpath('new_dir')
# os.rmdir(path)









