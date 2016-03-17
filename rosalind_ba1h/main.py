# Find all approcimate occurances of a pattern in a string
__author__ = 'Abdelrahman Hosny <abdelrahman.hosny@ieee.org>'

def hammingdistance(p1, p2):
    hammingdistance = 0
    for i in range(0, len(p1)):
        if p1[i] != p2[i]:
            hammingdistance += 1
    return hammingdistance

with open('rosalind_ba1h.txt', 'r') as file:
    pattern =file.readline().strip()
    text = file.readline().strip()
    d= int(file.readline().strip())

    positions = []
    for i in range(0, len(text) - len(pattern)):
        if hammingdistance(pattern, text[i:i+len(pattern)]) <= d:
            positions.append(i)

    print ' '.join(map(str, positions))