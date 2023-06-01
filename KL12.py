# import tkinter as tk
# import re
# loggin_pattern=re.compile(r"^\w{3,20}@[a-z]{2,10}\.[a-z]{2,6}$")
# nick_pattern=re.compile(r"^\w{4,8}$")
# password_pattern=re.compile(r"^\w{8,16}$")
# root=tk.Tk()
# root1=tk.Tk()
# root.geometry('400x400+700+500')
# root1.geometry('400x400+700+500')
# # root.configure(bg='blue')
# # root.configure(bg='#000')
# root.resizable(False,False)
# root1.resizable(False,False)
#
# def logining():
#     login=login_entry.get()
#     password=password_entry.get()
#     nick=nick_entry.get()
#     if loggin_pattern.search(login):
#         if password_pattern.search(password):
#             login_entry.config(bg='green')
#             password_entry.config(bg='green')
#
#             if nick_pattern.search(nick):
#                 login_entry.config(bg='green')
#                 password_entry.config(bg='green')
#
#             else:
#                 login_entry.config(bg='green')
#                 password_entry.config(bg='green')
#
#         else:
#             login_entry.config(bg='green')
#             password_entry.config(bg='red')
#
#     else:
#         login_entry.config(bg='red')
#         password_entry.config(bg='red')
#
#
# def logining1():
#     nick=nick_entry.get()
#
#     if nick_pattern.search(nick):
#         nick_entry.config(bg='green')
#     else:
#         nick_entry.config(bg='red')
#
#
# login_label=tk.Label(root, text='Login', font=('Arial',14), padx=50,fg='blue')
# login_label1=tk.Label(root1, text='Login', font=('Arial',14), padx=50,fg='blue')
# password_label=tk.Label(root,text='Password', font=('Arial',14), padx=50)
# nick_label=tk.Label(root1,text='Nick', font=('Arial',14), padx=50)
#
# login_entry=tk.Entry(root,font=('Arial',12),width=20,bg='black',fg='white')
# nick_entry=tk.Entry(root1,font=('Arial',12),width=20)
# password_entry=tk.Entry(root,font=('Arial',12),width=20,show='*')
#
# login_button=tk.Button(root,text='LOGIN',font=('Arial',16),width=12,command=logining)
# login_button1=tk.Button(root1,text='LOGIN',font=('Arial',16),width=12,command=logining1)
#
#
# root.grid_columnconfigure(0, minsize=150)
# root.grid_columnconfigure(1,minsize=250)
# root1.grid_columnconfigure(2,minsize=250)
# root.grid_rowconfigure(0,minsize=90)
# root.grid_rowconfigure(1,minsize=90)
# root1.grid_rowconfigure(2,minsize=90)
# login_button.grid(columnspan=2)
#
# login_label.grid(column=0, row=0,sticky='w')
# password_label.grid(column=0,row=1,sticky='w')
# nick_label.grid(column=0,row=2,sticky='w')
#
# login_entry.grid(column=1,row=0,sticky='w')
# password_entry.grid(column=1,row=1,sticky='w')
# nick_entry.grid(column=1,row=2,sticky='w')
# login_button.grid(column=0,row=3)
# login_button1.grid(column=0,row=3)
# root.mainloop()


# def sayUserHello(user): #Охоплююча ф-я
#     msg='hello ' + user
#     def showMsf(): #Вкладена ф-я
#         nonlocal msg
#         msg='Student'
#         print(msg+' lets start')
#     showMsf()
#     print(msg)
#
# sayUserHello('admin')

# def sayhello(user):
#     msg='Hi, ' + user
#     def show():
#         print(msg+' and world')
#
#     return show
#
# case1=sayhello('admin')
# case1()

# def doExercise1(var_1):
#     var_2=5
#     def doExercise2(var_2):
#         return var_1**var_2
#     return doExercise2
#
# case1=doExercise1(2)
# print(case1(5))
# print(case1(10))











