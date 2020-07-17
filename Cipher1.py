#
#  Cipher1.py
#  System Level Assignments
#
#  Created by Minh Nguyen on 7/12/20.
#  Copyright © 2020 Minh Nguyen. All rights reserved.
#
import sys

def main():
    if len(sys.argv) != 4:
        print("Please provide 3 inputs (space seperate) for this program:")
        print("   1. An integer key (1 - 26).")
        print("   2. A name of input file.")
        print("   3. A name of output file.")
        print("Please run the program again.")
        return

    key = int(sys.argv[1])
    while key < 1 or key > 26:
        print("Your key input: {}".format(key))
        key = input("The number must be between 1 and 26. Please try again: ")

    try:
        input = open(str(sys.argv[2]), "r")
    except IOError:
        print(str(sys.argv[2]) + " doesn't exist. Please try again.")
        input.close()

    print("Opening file " + input.name + "...")

    try:
        output = open(str(sys.argv[3]), "w")
    except IOError:
        print("Cannot open file " + str(sys.argv[3]))
        output.close()

    print("Opening file " + output.name + "...")

    print("Translating...")

    for read in input:
        line = ""
        for c in read:
            c = c.lower()
            if ord(c) >= ord('a') and ord(c) <= ord('z'):
                c = chr(int((ord(c) - ord('a') + key) % 26) + ord('a'))
            line += c
        print(line)
        output.write(line)

    print("Output is saved to " + output.name)

    input.close()
    output.close()

main()
