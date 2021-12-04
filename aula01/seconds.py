s = int(input("Segundos: "))

h = s // 3600
s = s % 3600

m = s // 60
s = s % 60

print("{:02d}:{:02d}:{:02d}".format(h, m, s))

proof = h*60*60 + m*60 + s
print(proof)
