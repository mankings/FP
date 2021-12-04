t = []
max = 0
min = 0
avg = 0

def inputFloatList():
    while True:
        s = input("Insira um número: ")
        if s == "": break
        p = int(s)
        t.append(p)
    print()
    print(t)

def countLower(lst, v):
    lower = []
    for n in range(len(lst)):
        if float(lst[n]) < v:
            lower.append(lst[n])
    print(lower)

def minmax(lst):
    max = lst[0]
    min = lst[0]
    for n in range(len(lst)):
        if lst[n] > max:
            max = lst[n]
    for n in range(len(lst)):
        if lst[n] < min:
            min = lst[n]
    
    avg = (min + max)/2

    print("Máximo:", max)
    print("Mínimo:", min)
    print("Média Max/Min:", avg)

inputFloatList()
minmax(t)
countLower(t, avg)