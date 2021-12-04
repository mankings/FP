def max2(x, y):
  if x > y:
    return x
  else:
    return y

def max3(x, y, z):
  if max(x, y) > max(y, z):
    return max(x, y)
  else:
    return max(y, z)

a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))

print("Máximo:", max3(a, b, c))

