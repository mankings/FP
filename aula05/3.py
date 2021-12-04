names = ["dez", "vinte", "trinta", "quarenta"]
tels = [10, 20, 30, 40]

def telToName(tel, names, tels):
    pos = 0
    for n in range(len(tels)):
        if tel == tels[n]:
            pos = n
    
    print(tel, names[pos])

def nameToTel(name, names, tels):
    pos = 0
    for n in range(len(names)):
        if name == names[n]:
            pos = n
    
    print(name, tels[pos])

telToName(20, names, tels)
nameToTel("dez", names, tels)