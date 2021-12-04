def avg():
    total = 0.0
    n = 0
    
    while True:
        x = input("Number? ")
        if x == "" : break
        n += 1
        total += float(x)
    
    total /= n
    
    print(total)
    
avg()
