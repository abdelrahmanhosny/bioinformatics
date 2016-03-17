# Computes the hamming distance between two strings
__author__ = 'Abdelrahman Hosny <abdelrahman.hosny@ieee.org>'

with open('rosalind_ba1g.txt', 'r') as file:
    genome1 =file.readline().strip()
    genome2 = file.readline().strip()
    hammingdistance = 0
    for i in range(0, len(genome1)):
        if genome1[i] != genome2[i]:
            hammingdistance += 1
    print hammingdistance