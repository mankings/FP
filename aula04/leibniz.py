n = int(input("n: "))
a = 1

for n in range(n):
    a += (-1)**n/(2*n + 1)
    print(a)
