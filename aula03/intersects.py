def intersects(a1, a2, b1, b2):
    if (b2 > a1 and b1 < a2) or (a2 > b1 and b2 > a1):
        return True
    else:
        return False


a1 = float(input("a1: "))
a2 = float(input("a2: "))
b1 = float(input("b1: "))
b2 = float(input("b2: "))

print(intersects(a1, a2, b1, b2))