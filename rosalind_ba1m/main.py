# Implement number to pattern function
__author__ = 'Abdelrahman Hosny <abdelrahman.hosny@ieee.org>'


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

with open('rosalind_ba1m.txt', 'r') as file:
    index = int(file.readline().strip())
    k = int(file.readline().strip())
    print numbertopattern(index, k)