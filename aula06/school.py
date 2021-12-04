# Complete o programa!

# a)
def loadFile(fname, lst):
    dataFile = open(fname, "r")
    lines = dataFile.read().splitlines()
    for i in range(len(lines)-1):
        line = tuple(lines[i+1].split("\t"))
        lst.append(line)
    dataFile.close()

# b) Crie a função notaFinal aqui...
def notaFinal(alunoIndex, lst):
    avg = (float(lst[alunoIndex][-1]) + float(lst[alunoIndex][-2]) + float(lst[alunoIndex][-3]))/3
    return avg

# c) Crie a função printPauta aqui...
def printPauta(lst, fname):
    print("{:>6}{:^50}{:>4}".format("Número", "Nome", "Nota"))
    for i in range(len(lst)):
        print("{:>6}{:^50}{:.1f}".format(lst[i][0], lst[i][1], notaFinal(i, lst)))

    pautaFile = open(fname, "w")
    pautaFile.write("{:>6}{:^50}{:>4}\n".format("Número", "Nome", "Nota"))
    for i in range(len(lst)):
        pautaFile.write("{:>6}{:^50}{:.1f}\n".format(lst[i][0], lst[i][1], notaFinal(i, lst)))
    pautaFile.close()

# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    # ordenar a lista
    lst = sorted(lst)
    lst = sorted(lst, key=lambda number: int(number[0]))

    # mostrar a pauta
    printPauta(lst, "pautaFinal.txt")


# Call main function
if __name__ == "__main__":
    main()


