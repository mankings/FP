def letterCounter(file):
    letters = {}
    for c in file:
        if (c.lower().isalpha()):
            if (c.lower() not in letters):
                letters[c.lower()] = 1
            else:
                letters[c.lower()] += 1

    lettersSorted = {k: v for k, v in sorted(letters.items(), key=lambda item: item[1], reverse = True)}
    
    for letter in lettersSorted.keys():
        print(letter, lettersSorted[letter])

name = "pg3333.txt"
with open(name, 'r') as ficheiro:
    fileToRead = ficheiro.read()
    letterCounter(fileToRead)
