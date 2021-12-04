def listInput():
    print("Create a list. Leave empty to end.")
    lst = []
    while True:
        a = input("Value to add to list: ")
        if a == "":
            print()
            break
        lst.append(int(a))
    
    sLst = sorted(lst)

    return sLst

def mediana(lst):
    l = len(lst)//2
    if(len(lst) % 2 == 0):
        a = lst[l - 1]
        b = lst[l]
        return ((a + b)/2)
    a = lst[l]
    return a

def main():
    data = listInput()
    print(data)
    print(mediana(data))

main()
    