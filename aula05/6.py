def shorten(s):
    short = ""
    for letter in s:
        if letter.isupper():
            short = short + letter
    return short

print(shorten(input("String: ")))