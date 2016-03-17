# Finds a position in the genome minimizing the skew
__author__ = 'Abdelrahman Hosny <abdelrahman.hosny@ieee.org>'

def skewi(genome):
    skew = []
    skew.append(0)
    for i in range(0, len(genome)):
        if genome[i] == 'C':
            skew.append(skew[i]-1)
        elif genome[i] == 'G':
            skew.append(skew[i]+1)
        else:
            skew.append(skew[i])
    return skew


with open('rosalind_ba1f.txt', 'r') as file:
    genome = file.readline().strip()
    skewvalues = skewi(genome)
    minimum = min(skewvalues)
    ivalues = []
    for i in range(0, len(skewvalues)):
        if skewvalues[i] == minimum:
           ivalues.append(i)
    print ' '.join(map(str, ivalues))