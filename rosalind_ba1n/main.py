# Generate the d-Neighborhood of a String
__author__ = 'Abdelrahman Hosny <abdelrahman.hosny@ieee.org>'

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


with open('rosalind_ba1n.txt', 'r') as file:
    pattern = file.readline().strip()
    d = int(file.readline().strip())
    print '\n'.join(neighbors(pattern, d))