# Find all distinct k-mers forming (L,t)-clumps in genome
__author__ = 'Abdelrahman Hosny <abdelrahman.hosny@ieee.org>'

'''
# this is a stupid implementation that takes a long time to run
def patterncount(text, pattern):
    count = 0
    for i in range(0, len(text)-len(pattern)):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count


def frequentwords(text, k, t):
    frequentpatterns = []
    count = []
    for i in range(0, len(text)-k):
        pattern = text[i:i+k]
        count.append(patterncount(text, pattern))
    for i in range(0, len(text)-k):
        if count[i] >= t:
            frequentpatterns.append(text[i:i+k])
    return list(set(frequentpatterns))
'''

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


def findclump(genome, k, t, L):
    frequentpatterns = []
    clump = [0] * (4**k)
    text = genome[0:L]
    frequencyarray = computefrequencies(text, k)
    for i in range(0, 4**k):
        if frequencyarray[i] >= t:
            clump[i] = 1
    for i in range(1, len(genome) - L + 1):
        firstpattern = genome[i-1:i-1+k]
        index = patterntonumber(firstpattern)
        frequencyarray[index] -= 1
        lastpattern = genome[i+L-k: i+L]
        index = patterntonumber(lastpattern)
        frequencyarray[index] += 1
        if frequencyarray[index] >= t:
            clump[index] = 1
    for i in range(0, 4**k):
        if clump[i] == 1:
            pattern = numbertopattern(i, k)
            frequentpatterns.append(pattern)

    return frequentpatterns


with open('rosalind_ba1e.txt', 'r') as file:
    genome = file.readline().strip()
    k, L, t = map(int, file.readline().strip().split(' '))
    clumps = findclump(genome, k, t, L)
    print ' '.join(list(set(clumps)))

