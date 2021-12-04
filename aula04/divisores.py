n = int(input("int: "))
x = 0

for d in range(1, n, 1):
    if n % d == 0:
        print(d)
        x += d

if x < n:
    print("Deficiente.", x)
elif x == n:
    print("Perfeito.", x)
else:
    print("Abundante.", x)