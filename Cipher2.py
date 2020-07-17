#
#  Cipher1.py
#  System Level Assignments
#
#  Created by Minh Nguyen on 7/12/20.
#  Copyright © 2020 Minh Nguyen. All rights reserved.
#
import sys

def main():
    if len(sys.argv) != 2:
        print("Please provide 1 inputs (space seperate) for this program:")
        print("   1. A name of input file.")
        print("Please run the program again.")
        return

    try:
        input = open(str(sys.argv[1]), "r")
    except IOError:
        print(str(sys.argv[1]) + " doesn't exist. Please try again.")
        input.close()

    print("Reading file " + input.name + "...")

    letters = [0] * 26

    for read in input:
        for c in read:
            c = c.lower()
            if ord(c) >= ord('a') and ord(c) <= ord('z'):
                letters[ord(c) - ord('a')] += 1
        print(read)

    print("Report:")
    max1 = max2 = 0
    letter1 = letter2 = -1
    for i in range(len(letters)):
        print(chr(i + ord('a')) + ": " + str(letters[i]))
        if letters[i] > max1:
            letter1 = i
            max1 = letters[i]
        elif letters[i] > max2 and i != letter1:
            max2 = letters[i]
            letter2 = i

    print("Found the most common letter is " + chr(letter1 + ord('a')) + " (" + str(max1) + ")")
    print("Found the second most common letter is " + chr(letter2 + ord('a')) + " (" + str(max2) + ")")

    mostCommonLetter = ord('e') - ord('a')
    secondCommonLetter = ord('t') - ord('a')

    key1 =  key2 = 0

    key1 = mostCommonLetter - letter1
    if key1 < 0: key1 += 26

    key2 = secondCommonLetter - letter2
    if key2 < 0: key2 += 26

    print("Key 1: " +  str(key1))
    print("Key 2: " +  str(key2))
    if key1 == key2:
        print("Possible key: " +  str(key1))

    input.close()

main()
