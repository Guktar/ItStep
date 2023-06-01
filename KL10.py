# a=2
# print(f'id(2) - {id(a)}')
# print(f'id(a) - {id(a)}')
# a=a+1
# print(f'id(a) - {id(a)}')
# print(f'id(3) - {id(3)}')
#
# b=2
# print(f'id(b) - {id(b)}')
# print(f'id(2) - {id(2)}')
#
# c=3
# print(f'id(c) - {id(c)}')
# print(f'id(3) - {id(3)}')

#local - Всередені функції
#enlosing - Область відімості коли у нас внутрі однієї функції є ще одна
#global - а=2
#built-in Зарезервиване значенням Python

#LEGB - local -> enlosing -> global ->built-in Послідовність пошуку

#var_1=5
# def func_1():
#     global var_1
#     var_1=10
#     print(f'var_1 in function - {var_1}')
#
# func_1()
# print(var_1)
# var_1=5
# def func_2():
#     var_1=2
#     print(var_1)
# var_1=5
# def func_3():
#     var_1=10
#     def func_4():
#         print(var_1)
#
#     func_4()
# func_3()
# print(var_1)
#
# var_2=15
# var_1=6
# def first():
#     var_1=10
#
#     def second():
#         nonlocal var_1
#         var_1=1
#         global var_2
#         var_2=3
#         print(locals())
#     second()
#     print(var_1)
# first()
# print(var_2)
# print(var_1)
#
# print(f'local - {locals()}')
# print(f'global - {globals()}')
#
# print(locals())
# print(globals())

#args - для позиційних аргументів
#kwargs - для іменованих аргументів

#
# def black_hole(*args):
#     print(type(args))
#     for argument in args:
#         print(argument)
#
# # args=3,5,18,'name','address',4*5
#
# black_hole(3,5,18,'name','address',4*5)
#
# def black_hol_name(**kwargs):
#     print(type(kwargs))
#     for argument in kwargs:
#         print(argument)
#     for key, value in kwargs.items():
#         print(key,value,sep=':')
# black_hol_name(name='Nick',auto='BMW',age=15,school=217)
#
# a=12
# c=34
# b=56
# print(a,b,c,sep='-->')

def black_hole_full(*args,**kwargs):
    for arg in args:
        print(arg)
    for key,value in kwargs.items():
        print(key,value,sep=' : ')

black_hole_full(23,'auto',5*3,name='Nik',school=217)

def black_hole_mixed(var_1,var_2,*args,**kwargs):
    print(f'var_1 - {var_1}')
    print(f'var_2 - {var_2}')
    for arg in args:
        print(arg)
    for key,value in kwargs.items():
        print(key,value,sep=':')

black_hole_mixed(23,'auto',5*3,45,name='Nik',school=217)



def way(v,t):
    s=v*t
    print(s)

lst=[80,3]

way(*lst)

dict_1={'t':3, 'v':80}

def way(v,t):
    s=v*t
    print(s)

way(**dict_1)

dict_2={'var_3':5,'var_4':12}
lst_1=[2]
def some(var_1,var_2,var_3,var_4):
    print(var_1,var_2,var_3,var_4)

some(1,*lst_1,**dict_2)


