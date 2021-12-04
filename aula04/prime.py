def isPrime(n):
    prime = True
    for d in range(2, n, 1):
        if n % d == 0 and n != d and d != 1:
            prime = False
            break
        elif n == 1 or n == 2:
            prime = True
        else:
            prime = True
            
    if(prime):
        print("{:3d}".format(n), "is prime")
    else:
        print("{:3d}".format(n), "is not prime.")

for x in range(1, 101, 1):
    isPrime(x)
