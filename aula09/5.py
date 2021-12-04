import bisect

def wordSearch(snip, words):
    wordList = []
    bisect.bisect_left(snip, words)

    return wordList

def main():
    with open("wordlist.txt") as file:
        allWords = file.read().splitlines()
        print(wordSearch(input("Words starting with: "), allWords))

main()