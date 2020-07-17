#
# Simple Tasks in Python
# System Level Assignments
#
# Created by Minh Nguyen 7/16/2020.
#

import re

def task1():
    string = input("Hello. Say something and I read it out loud: ")
    print("You said: " + string)


def task2():
    string = input("Give me an integer: ")
    num = int(string)
    print("You entered " + str(num))
    print("To prove it's an integer, I added 5 to it: " + str(num + 5))

def isLeapYear(year):
    if year % 400 == 0: return True
    if year % 4 == 0 and year % 100 != 0: return True
    return False

def task3():
    year = input("Give me a year: ")
    if isLeapYear(int(year)):
        print(str(year) + " is a leap year")
    else:
        print(str(year) + " is NOT a leap year")

def task4():
    sum = 0
    for i in range(1, 1000):
        if i % 3 ==0 or i % 5 ==0:
            sum += i
    print("Sum of all integers that is below 1000 is: " + str(sum))

def isPalindrome(string):
    length = len(string)
    for i in range(int(length / 2)):
        if string[i] != string[-1 - i]:
            return False
    return True

def task5():
    for a in range(999, 9, -1):
        for b in range(a, 9, -1):
            if isPalindrome(str(a * b)):
                print("The max palindrome is: " + str(a * b))
                return

def numberToWord(num):
    result = ""
    if num <= 19:
        words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
                 "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        result += words[num]
    elif num < 100:
        first = int(num / 10)
        second = int(num % 10)
        wordsFirst = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        wordsSecond = ["", "-one", "-two", "-three", "-four", "-five", "-six", "-seven", "-eight", "-nine"]
        result += wordsFirst[first]
        result += wordsSecond[second]
    return result

def task6():
    num = input("Give me an  integer (less than 100): ")
    print(str(num) + " has been converted to words: " + numberToWord(int(num)))

def wordsToNumber(string):
    result = 0
    word = re.split('- |-', string.lower())
    if len(word) == 1:
        words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
                 "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        for i in range(len(words)):
            if word[0] == words[i]:
                result = i
                break
    else:
        wordsFirst = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        wordsSecond = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        for i in range(len(wordsFirst)):
            if word[0] == wordsFirst[i]:
                result = i * 10
                break
        for i in range(len(wordsSecond)):
            if word[1] == wordsSecond[i]:
                result += i
                break
    return result


def task7():
    string = input("Give me a number in words: ")
    print(str(string) + " has been converted to number: " + str(wordsToNumber(string)))

def task8():
    string = input("Give me two numbers in words: ")
    words = string.split(" ")
    a = wordsToNumber(words[0])
    b = wordsToNumber(words[1])
    print(str(a) + " * " + str(b) + " = " + str(a * b))

def main():
    print("Task 1:")
    task1()
    print("\n")

    print("Task 2:")
    task2()
    print("\n")

    print("Task 3:")
    task3()
    print("\n")

    print("Task 4:")
    task4()
    print("\n")

    print("Task 5:")
    task5()
    print("\n")

    print("Task 6:")
    task6()
    print("\n")

    print("Task 7:")
    task7()
    print("\n")

    print("Task 8:")
    task8()
    print("\n")

main()
