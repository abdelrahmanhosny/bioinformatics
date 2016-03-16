# Implement pattern to number function
__author__ = 'Abdelrahman Hosny <abdelrahman.hosny@ieee.org>'


def symboltonumber(symbol):
    if symbol == 'A':
        return 0
    elif symbol == 'C':
        return 1
    elif symbol == 'G':
        return 2
    elif symbol == 'T':
        return 3


def patterntonumber(pattern):
    if pattern == "":
        return 0
    return 4 * patterntonumber(pattern[:-1]) + symboltonumber(pattern[len(pattern)-1])


with open('rosalind_ba1l.txt', 'r') as file:
    pattern = file.readline().strip()
    print patterntonumber(pattern)