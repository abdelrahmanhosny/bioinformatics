# Compute frequency array of k-mers in a text
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


def computefrequencies(text, k):
    frequencyarray = []
    for i in range(0, 4**k):
        frequencyarray.append(0)
    for i in range(0, len(text) - k + 1):
        frequencyarray[patterntonumber(text[i:i+k])] += 1
    return frequencyarray

with open('rosalind_ba1k.txt', 'r') as file:
    text = file.readline().strip()
    k = int(file.readline().strip())
    print ' '.join(map(str, computefrequencies(text, k)))

