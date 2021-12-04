def fibonacci(n):
    n1 = 0
    n2 = 1
    x = 0
    
    if n == 1:
        return(n1)
    elif n == 2:
        return(n1 + n2)
    else:
        for n in range(n-1):
            x = n1 + n2
            n1 = n2
            n2 = x
    
    return(x)

n = int(input("int: "))
print(fibonacci(n))
