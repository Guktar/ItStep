#Двійкові файли
#документи і електронні таблиці .doc, .pdf, .xls
#архіви .zip, .7z, .rar, .iso
#бази даних .db .ndb .sqllite, .accde
#виконувальні файли .exe, .dll
#зображення .png . jpeg
#аудіо .mp3 .mka
#відео .mp4 .avi


#Текстові файли
#Текстові документи .txt .rtf .tex
#файли початкових кодів .py .js .java .c
#Веб документи і стандарти .json .html .css .xml
#Файли налаштувань та конфігурацій .cfg .ini

#Відкриття файлу
#Читання з файлу
#Запис у файл
#Видалення файлу

#fileObj=open(fileName,mode)
#r-лише для читання
#w-лише для змінни
#а-для додавання
#r+ - для читання і запису
#w+ - для змінни і запису
#a+ - для додавання і запису
#rb - відкриття 2-го файлу на читання
#wb
#ab
#wb+
#ab+


# f1=open('C:\\Users\\ihor.verbytskyi\\Desktop\\ItStep\\KL\\Files\\myFile.txt','r')
# s1=f1.readline() #Прочитати строку
# print(s1)
# s2=f1.readline()
# print(s2)
# f1=open('C:\\Users\\ihor.verbytskyi\\Desktop\\ItStep\\KL\\Files\\myFile.txt','r')
# # print(f1.read()) #read - читання
# print(f1.read(4)) #read(n) - т-к-ть символів для читання
# print(f1.read())

# f1=open('C:\\Users\\ihor.verbytskyi\\Desktop\\ItStep\\KL\\Files\\myFile.txt','r')
# lines=f1.readlines() #зчитати файл у список рядків
# print(lines)

# f1=open('C:\\Users\\ihor.verbytskyi\\Desktop\\ItStep\\KL\\Files\\myFile.txt','r')
# for line in f1:
#     print(line)

# f2=open('C:\\Users\\ihor.verbytskyi\\Desktop\\ItStep\\KL\\Files\\myFile2.txt','w')
# n=f2.write('Some text')

# import random
#
# i=0
# spysok=[]
# while i<10:
#     chislo=random.randint(0,1001)
#     spysok+=[chislo]
#     i+=1
# print(spysok)
#
# f=open('C:\\Users\\ihor.verbytskyi\\Desktop\\ItStep\\KL\\Files\\spysok.txt','w')
# s=str(len(spysok))
# f.write(s+'\n')
# for i in spysok:
#     s=str(i)
#     f.write(s+' ')
# f.close()
# f=open('C:\\Users\\ihor.verbytskyi\\Desktop\\ItStep\\KL\\Files\\spysok.txt','r')
# lines=f.readlines()
# print(lines)
# spysok_txt=['asdasd','asdas','asdasd','qweqwads','rtytr']
# f=open('C:\\Users\\ihor.verbytskyi\\Desktop\\ItStep\\KL\\Files\\spysok_strok.txt','w')
# for line in spysok_txt:
#     f.write(line+'\n')
#
# f.close()

# spysok_txt=['asdasd','asdas','asdasd','dass','rtdsr']
# f=open('C:\\Users\\ihor.verbytskyi\\Desktop\\ItStep\\KL\\Files\\spysok_strok.txt','a')
# for line in spysok_txt:
#     f.write(line+'\n')
#
# f.close()

# slovnyk={1:'Mon',2:'Tue',3:'Wed',4:'Thu',5:'Fri'}
# f=open('C:\\Users\\ihor.verbytskyi\\Desktop\\ItStep\\KL\\Files\\slovnyk.txt','w')
# for item in slovnyk:
#     s=str(item)
#     s+=':'
#     s+=slovnyk.get(item)
#     s+='\n'
#     f.write(s)
# f.close()

# f1=open('C:\\Users\\ihor.verbytskyi\\Desktop\\ItStep\\KL\\Files\\myFile.txt','r')
#
# count=0
# s=f1.readline()
# while s!='':
#     s=f1.readline()
#     count+=1
# print(count)

# f2=open('C:\\Users\\ihor.verbytskyi\\Desktop\\ItStep\\KL\\Files\\myFile.txt','r')
# spysok=f2.readlines()
# count=len(spysok)
# print(count)

# f3=open('C:\\Users\\ihor.verbytskyi\\Desktop\\ItStep\\KL\\Files\\python.txt','r')
# s=input('Enter text for change: ')
# pos=2
# spysok=f3.readlines()
# if (pos>=0) and (pos<len(spysok)):
#     if (pos==len(spysok)-1):
#         spysok[pos]=s
#     else:
#         spysok[pos] = s+ '\n'
# f3.close()
# f3=open('C:\\Users\\ihor.verbytskyi\\Desktop\\ItStep\\KL\\Files\\python.txt','w')
# for line in spysok:
#     f3.write(line)
# f3.close()

# pos=int(input('Pos = '))
# f=open('C:\\Users\\ihor.verbytskyi\\Desktop\\ItStep\\KL\\Files\\python.txt','r')
# spysok=f.readlines()
# if (pos>=0) and (pos<len(spysok)):
#     i=pos
#     while i<len(spysok)-1:
#         spysok[i]=spysok[i+1]
#         i+=1
#     spysok=spysok[:-1]
# f.close()
# f=open('C:\\Users\\ihor.verbytskyi\\Desktop\\ItStep\\KL\\Files\\python.txt','w')
# for line in spysok:
#     f.write(line)
# f.close()

f1=open('C:\\Users\\ihor.verbytskyi\\Desktop\\ItStep\\KL\\Files\\myFile.txt','r')
f2=open('C:\\Users\\ihor.verbytskyi\\Desktop\\ItStep\\KL\\Files\\myFile2.txt','r')

spysok1=f1.readlines()
spysok2=f2.readlines()
spysok3=spysok1+['\n']+spysok2
f1.close()
f2.close()

f3=open('C:\\Users\\ihor.verbytskyi\\Desktop\\ItStep\\KL\\Files\\union.txt','w')
for i in spysok3:
    f3.write(i)
f3.close()













