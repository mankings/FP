def letterCounter(file):
    letters = {}
    for c in file:
        if (c.lower().isalpha()):
            if (c.lower() not in letters):
                letters[c.lower()] = 1
            else:
                letters[c.lower()] += 1
    
    for letter in sorted(letters.keys):
        print(letter, letters[letter])

name = "pg3333.txt"
with open(name, 'r') as ficheiro:
    fileToRead = ficheiro.read()
    letterCounter(fileToRead)
