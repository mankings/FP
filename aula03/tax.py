def tax(r):
    if r <= 1000:
        tax = 0.1*r
    elif r <= 2000:
        tax = 0.2*r - 100
    else:
        tax = 0.3*r - 300

    return tax


a = float(input("Tax: "))
print(tax(a))
