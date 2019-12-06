import pyperclip

def data():

    source = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя —1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()-_=+"№[]{};:|/<>,.'

    dict = {}
    n = 0

    for x in source:
        dict[n] = x
        n += 1

    return dict

def chrToNum(text):
    list = []
    d = data()
    for x in range(len(text)):
        for j in d:
            if text[x] == d[j]:
                list.append(j)
                break

    return list

def NumToChr(list):

    dict = data()
    res = []

    for x in list:
        res.append(dict[x])

    return ''.join(res)

def dPrint():
    print(data())

def encoding(text,password):
    lRes = []
    lText = chrToNum(text)
    lPassword = chrToNum(password)
    dDict = {}
    i = 0
    j = 0

    for x in lText:
        dDict[i] = [x,lPassword[j]]
        i+=1
        j+=1
        if j >= len(lPassword):
            j = 0

    for x in dDict:
        lRes.append((dDict[x][0]+dDict[x][1]) % len(data()))

    return NumToChr(lRes)

def fDecode(text,key):
    t = chrToNum(text)
    k = chrToNum(key)
    d = data()
    dDict = {}
    j,i = 0,0

    res = []

    for x in t:
        dDict[i] = [x,k[j]]
        i+=1
        j+=1
        if j >= len(k):
            j = 0

    for x in dDict:
        res.append((dDict[x][0]-dDict[x][1]+len(d)) % len(data()))

    return res

def decode(text,key):
    return NumToChr(fDecode(text,key))


# MAIN

from tkinter import *

def changeModeCommand():
    if changeModeBtn['text'] == 'EN':
        changeModeBtn['text'] = 'DE'
    else:
        changeModeBtn['text'] = 'EN'

def encryptCommand():
    text2.delete(1.0, END)
    text2.insert(1.0,encoding(text1.get(1.0,END),keyField.get()))


root = Tk()
root.title('Encoder')
root.geometry('400x420')
root.resizable(False,False)

changeModeBtn = Button(root, text='DE', width=4, height=2,font=("Segoe UI", 8, 'bold'), command=changeModeCommand)
keyField = Entry(width='30')
keyLabel = Label(text='Ключ:', font=("Segoe UI", 8, 'bold'))
encryptBtn = Button(text='Зашифровать',height=2,font=("Segoe UI", 8, 'bold'),command=encryptCommand)

frame1 = Frame(root)
l1 = Label(frame1,text='Исходный текст',font=("Segoe UI", 10, 'bold'))
l1.pack()
text1 = Text(frame1, width=44,height=9)
text1.pack(side=LEFT,padx=2)
scroll = Scrollbar(frame1,command=text1.yview)
scroll.pack(side=LEFT, fill=Y)
frame1.grid(row=1,column=0,columnspan=6)
text1.config(yscrollcommand=scroll.set)

frame2 = Frame(root)
l2 = Label(frame2,text='Зашифрованный текст',font=("Segoe UI", 10, 'bold'))
l2.pack()
text2 = Text(frame2, width=44,height=9)
text2.pack(side=LEFT,padx=2)
scroll = Scrollbar(frame2,command=text2.yview)
scroll.pack(side=LEFT, fill=Y)
frame2.grid(row=2,column=0,columnspan=6,pady=10)
text2.config(yscrollcommand=scroll.set)

encryptBtn.grid(row=0,column=1,padx=5,pady=10, sticky=W)
changeModeBtn.grid(row=0, column=0, padx=5,pady=5, sticky=W)
keyLabel.grid(row=0, column=2,padx=5,pady=5, sticky=E)
keyField.grid(row=0, column=3,columnspan=3,padx=5,pady=18, sticky=N+S+E+W)
root.mainloop()
