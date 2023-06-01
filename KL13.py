# spysok=[2,4,7,12,34,1,56,78,9]
# # b=0
# # for i in spysok:
# #    b+=i
# #
# # print(b)
#
# def calcSum(A):
#     if A==[]:
#         return 0
#     else:
#         summ=calcSum(A[1:])
#         summ+=A[0]
#         return summ
#
# summ=calcSum(spysok)
# print(summ)

# spysok=[1,-7,9,15,25,-67,-98,-56,65]
# def calcSumNegative(A):
#     if A==[]:
#         return 0
#     else:
#         count=calcSumNegative(A[1:])
#         if A[0]<0:
#             count+=1
#
#         return count
#
# n=calcSumNegative(spysok)
# print(n)

# def GetFibonaccilist(n,l):
#     count=len(l)
#     if len(l)<2:
#         return []
#     num1=l[count-2]
#     num2=l[count-1]
#     if (num1+num2)<n:
#         l=l+[num1+num2]
#         return GetFibonaccilist(n,l)
#     else:
#         return l
# new=GetFibonaccilist(100,[0,1])
# print(new)

# def Power(x,y):                  #1. Power(3,4) ... #1.2.3.4 3*3*3*3
#     if y>0:                      #1. 4>0 ->
#         return x*Power(x,y-1)    #1. 3*Power(3,3)
#     else:
#         return 1
#
# x=3
# y=4
# res=Power(x,y)
# print(res)

# def GetMaxList(L):
#     if len(L)>1:
#         Max=GetMaxList(L[1:])
#         if L[0]<Max:
#             return Max
#         else:
#             return L[0]
#     if len(L)==1:
#         return L[0]
# spysok=[500,6000,40,53]
# res=GetMaxList(spysok)
# print(res)

# a=int(input('К-ть елементів'))
# i=0
# b=[]
# while i<a:
#     s=int(input('chislo'))
#     b+=[s]
#     i+=1
# print(b)

# def simpledecorator(myFunction):
#     print('Hello! I am decorator')
#     def simpleWrapper():
#         print('Functions starts working.....')
#         myFunction()
#         print('See you!')
#     return simpleWrapper()
#
# def simpledecorator_v2(myFuncton):
#     print('Hello i am second decorator')
#     def simpleWrapper():
#         print('Lets start ....')
#         myFuncton()
#         print('Good luck')
#     return simpleWrapper
#
# @simpledecorator_v2
# @simpledecorator
#
# def sayHi():
#     print('Welcome')
# sayHi()
# #simpledecorator(sayHi)
#
# def sayBye():
#     print('Bye')
# sayBye=simpledecorator(sayBye)
# sayBye()

# def simpleDecotator_v3(myFunction):
#     print('I m 3rd decorator')
#     def simpleWrapper():
#          print('Functions starts working.....')
#          result1=myFunction()
#          print('See you!')
#          return result1
#     return simpleWrapper
#
# def calculateSum():
#     print('Welcome! lets start calculate')
#     x=int(input('X: '))
#     y=int(input('Y: '))
#     return x+y
# a=simpleDecotator_v3(calculateSum)
# print(a())

# def simpleDecotator_v4(myFunction):
#     print('Hello! Im fourth Decorator')
#     def simpleWrapper(argX, argY):
#         print('I have got {}, {}. Functions start working ....'.format(argX,argY))
#         result1=myFunction(argX,argY)
#         print('See you')
#         return result1
#     return simpleWrapper
#
# def calculateSum(a,b):
#     print('Welcome! lets start calculate')
#     x=int(input('X: '))
#     y=int(input('Y: '))
#     return x+y+a+b
# a=simpleDecotator_v4(calculateSum)
# print(a(3,4))




















