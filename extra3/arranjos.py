# NMEC: 
# NOME: 

# Complete...
def arranjos(n, k):
    assert k >= 0
    assert k <= n
    if k == 0:
        return 1
    else:
        return n*arranjos(n-1, k-1)

def main():
    print(arranjos(2, 1))
    print(arranjos(5, 2))
    print(arranjos(5, 3))
    print(arranjos(10, 3))

main()