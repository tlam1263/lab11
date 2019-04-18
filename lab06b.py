"""
Program: CS 115 Lab 6b
Author: Your name
Description: Computes the average word length of the user's text.
"""


def main():
    letters = 0
    infinite = 0
    words = 0

    c = str(input('Enter some text: '))
    b = c.split()
    words = words + len(b)
    if c == "":
        print("You did not enter any words.")
        quit()
    for i in range(len(b)):
        letters = letters + len(b[i])

    while infinite == 0:
        c = str(input('Enter some text: '))
        b = c.split()
        words = words + len(b)
        if c == "":
            infinite = infinite + 1
        for i in range(len(b)):
            letters = letters + len(b[i])

    a = letters/words

    print("The average word length is:", round(a, 5))


main()
