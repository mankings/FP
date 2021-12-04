import math as m

x1 = float(input("x1? "))
y1 = float(input("y1? "))
x2 = float(input("x2? "))
y2 = float(input("y2? "))

P = [x1, y1]
Q = [x2, y2]

d = m.dist(P, Q)

print(d)
