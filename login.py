import tkinter as tk
import re
loggin_pattern=re.compile(r"^\w{3,20}@[a-z]{2,10}\.[a-z]{2,6}$")
nick_patern=re.compile(r'^\w{4,8}$')
password_pattern=re.compile(r"^\w{8,16}$")
root=tk.Tk()
root.geometry('400x400+700+500')
# root.configure(bg='blue')
# root.configure(bg='#000')
root.resizable(False,False)

def logining():
    login=login_entry.get()
    password=password_entry.get()
    nick=nick_entry.get()
    if loggin_pattern.search(login):
        if password_pattern.search(password):
            login_entry.config(bg='green')
            password_entry.config(bg='green')
            nick_entry.config(bg='green')
            if nick_patern.search(nick):
                login_entry.config(bg='green')
                password_entry.config(bg='green')
                nick_entry.config(bg='green')
            else:
                login_entry.config(bg='green')
                password_entry.config(bg='green')
                nick_entry.config(bg='red')
        else:
            login_entry.config(bg='green')
            password_entry.config(bg='red')
            nick_entry.config(bg='red')

    else:
        login_entry.config(bg='red')
        password_entry.config(bg='red')
        nick_entry.config(bg='red')

login_label=tk.Label(root, text='Login', font=('Arial',14), padx=50,fg='blue')
password_label=tk.Label(root,text='Password', font=('Arial',14), padx=50)
nick_label=tk.Label(root,text='Password', font=('Arial',14), padx=50)

login_entry=tk.Entry(root,font=('Arial',12),width=20,bg='black',fg='white')
password_entry=tk.Entry(root,font=('Arial',12),width=20,show='*')
nick_entry=tk.Entry(root,font=('Arial',12),width=20)

login_button=tk.Button(root,text='LOGIN',font=('Arial',16),width=12,command=logining)


root.grid_columnconfigure(0, minsize=150)
root.grid_columnconfigure(1,minsize=250)
root.grid_rowconfigure(0,minsize=90)
root.grid_rowconfigure(1,minsize=90)
root.grid_rowconfigure(2,minsize=90)
login_button.grid(columnspan=3)

login_label.grid(column=0, row=0,sticky='w')
password_label.grid(column=0,row=1,sticky='w')
nick_label.grid(column=0,row=2,sticky='w')

login_entry.grid(column=1,row=0,sticky='w')
password_entry.grid(column=1,row=1,sticky='w')
nick_entry.grid(column=1,row=2,sticky='w')
login_button.grid(column=0,row=3)
root.mainloop()


