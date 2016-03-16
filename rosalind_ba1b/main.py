# Algorithms for finding the most frequent k-mers in a string
__author__ = 'Abdelrahman Hosny <abdelrahman.hosny@ieee.org>'


# Straightforward algorithm
def patterncount(text, pattern):
    count = 0
    for i in range(0, len(text)-len(pattern)):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count


def frequentwords(text, k):
    frequentpatterns = []
    count = []
    for i in range(0, len(text)-k):
        pattern = text[i:i+k]
        count.append(patterncount(text, pattern))
    maxcount = max(count)
    for i in range(0, len(text)-k):
        if count[i] == maxcount:
            frequentpatterns.append(text[i:i+k])
    return list(set(frequentpatterns))


# inherited from 1k
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

# inherited from 1m
def numbertosymbol(index):
    if index == 0:
        return 'A'
    elif index == 1:
        return 'C'
    elif index == 2:
        return 'G'
    elif index == 3:
        return 'T'

def numbertopattern(index, k):
    if k == 1:
        return numbertosymbol(index)
    prefixindex = index / 4
    r = index % 4
    symbol = numbertosymbol(r)
    prefixpattern = numbertopattern(prefixindex, k-1)
    return prefixpattern + symbol

# a faster algorithm
def fasterfrequentwords(text, k):
    frequentpatterns = []
    frequencyarray = computefrequencies(text, k)
    maxcount = max(frequencyarray)
    for i in range(0, 4**k):
        if(frequencyarray[i] == maxcount):
            frequentpatterns.append(numbertopattern(i, k))

    return frequentpatterns

with open('rosalind_ba1b.txt', 'r') as file:
    text = file.readline().strip()
    k = int(file.readline().strip())
    print ' '.join(fasterfrequentwords(text, k))
    print ' '.join(frequentwords(text, k))
    print set(fasterfrequentwords(text, k)) == set(frequentwords(text, k))