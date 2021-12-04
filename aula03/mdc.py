def mdc(a, b):
    r = a%b
    if r == 0:
        return b
    else:
        mdc(b, r)

a = int(input("a: "))
b = int(input("b: "))
print(mdc(a, b))