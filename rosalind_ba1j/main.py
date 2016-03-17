# Find the most frequent k-mers with mismatches in a string
__author__ = 'Abdelrahman Hosny <abdelrahman.hosny@ieee.org>'

# inherited from 1l
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

# inherited from 1n
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


# ingerited from 1n
def hammingdistance(p1, p2):
    hammingdistance = 0
    for i in range(0, len(p1)):
        if p1[i] != p2[i]:
            hammingdistance += 1
    return hammingdistance

def neighbors(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ["A", "C", "G", "T"]
    neighborhood = []
    suffixneighbors =  neighbors(pattern[1:], d)
    for text in suffixneighbors:
        if hammingdistance(pattern[1:], text) < d:
            for x in ['A', 'C', 'G', 'T']:
                neighborhood.append(x+text)
        else:
            neighborhood.append(pattern[0]+text)
    return neighborhood


# inherited from 1c
def reversecomplement(dna):
    reverse = ''
    for char in dna:
        if char == 'A':
            reverse += 'T'
        elif char == 'T':
            reverse += 'A'
        elif char == 'G':
            reverse += 'C'
        else:
            reverse += 'G'
    return reverse[::-1]

def approximatepatterncount(text, pattern, d):
    count = 0
    for i in range(0, len(text) - len(pattern) + 1):
        patterndash = text[i:i+len(pattern)]
        if hammingdistance(pattern, patterndash) <= d:
            count +=1
    return count


def frequentwordswithmismatch(text, k, d):
    frequentpatterns = []
    frequencyarray = [0] * (4**k)
    close = [0] * (4**k)
    for i in range(0, len(text) - k + 1):
        neighborhood = neighbors(text[i:i+k], d)
        for pattern in neighborhood:
            index = patterntonumber(pattern)
            close[index] = 1
    for i in range(0, 4**k):
        if close[i] == 1:
            pattern = numbertopattern(i, k)
            frequencyarray[i] = approximatepatterncount(text, pattern, d) + approximatepatterncount(text, reversecomplement(pattern), d)
    maxcount = max(frequencyarray)
    for i in range(0, 4**k):
        if frequencyarray[i] == maxcount:
            pattern = numbertopattern(i, k)
            frequentpatterns.append(pattern)
    return frequentpatterns


with open('rosalind_ba1j.txt', 'r') as file:
    text = file.readline().strip()
    k, d = map(int, file.readline().strip().split(' '))
    print ' '.join(frequentwordswithmismatch(text, k, d))