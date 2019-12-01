def data():

    source = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()-_=+"№[]{};:|/<>,.'

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

# MAIN

text = input('Введите текст: ')
key = input('Введите ключ: ')

print(encoding(text,key))

input('Press ENTER to exit')
