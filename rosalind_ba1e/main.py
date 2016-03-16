# Find all distinct k-mers forming (L,t)-clumps in genome
# WARNING: this is a very stupid implementation and takes long time to run!
__author__ = 'Abdelrahman Hosny <abdelrahman.hosny@ieee.org>'


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


with open('rosalind_ba1e.txt', 'r') as file:
    genome = file.readline().strip()
    k, L, t = map(int, file.readline().strip().split(' '))
    clumps = []
    for i in range(0, len(genome)-L):
        text = genome[i:i+L]
        clumps.extend(frequentwords(text, k, t))
    print ' '.join(list(set(clumps)))

