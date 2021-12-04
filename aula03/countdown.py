def countdown(n):
    while n > 0:
        print(n)
        if n > 0:
            n -= 1

n = int(input("n: "))
countdown(n)