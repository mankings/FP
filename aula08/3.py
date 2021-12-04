def main():
    dic = {}
    with open("names.txt", "r") as names:
        lines = names.read().splitlines()
        del lines[0]

        for line in lines:
            name = line.split()
            if(name[-1] in dic):
                dic[name[-1]].add(name[0])
            elif(name[-1] not in dic):
                dic[name[-1]] = set()
                dic[name[-1]].add(name[0])

    for surname, names in dic.items():
        print("{}: {}".format(surname, names))

main()