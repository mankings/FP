# Complete the code to make the HiLo game...

import random


def main():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101);
    print("Can you guess my secret?")
    
    x = int(input("Guess: "))
    
    while x != secret:
        if x < secret:
            print("Too low!")
        if x > secret:
            print("Too high!")
        x = int(input("Guess: "))
            
    if x == secret:
        print("Correct")

main()
