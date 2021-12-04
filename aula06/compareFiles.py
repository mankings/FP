def compareFiles(f1, f2):
    file1 = open(f1, "rb")
    file2 = open(f2, "rb")
    filesAreEqual = True

    while True:
        line1 = file1.read(1024)
        line2 = file2.read(1024)

        if(line1 != line2):
            filesAreEqual = False
            break
    
    file1.close()
    file2.close()
    
    return filesAreEqual

print(compareFiles(input("File1: "), input("File2: ")))