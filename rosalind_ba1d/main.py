# find pattern positions in a given genome
__author__ = 'Abdelrahman Hosny <abdelrahman.hosny@ieee.org>'

def patternpositions(pattern, genome):
    positions = []
    for i in range(0, len(genome)-len(pattern)):
        if genome[i:i+len(pattern)] == pattern:
            positions.append(str(i))
    return positions

with open('rosalind_ba1d.txt', 'r') as file:
    pattern = file.readline().strip()
    genome = file.readline().strip()
    print ' '.join(patternpositions(pattern, genome))