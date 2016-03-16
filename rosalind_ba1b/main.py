# A straightforward algorithm for finding the most frequence k-mers in a string
__author__ = 'Abdelrahman Hosny <abdelrahman.hosny@ieee.org>'


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

with open('rosalind_ba1b.txt', 'r') as file:
    text = file.readline()
    k = int(file.readline())
    print ' '.join(frequentwords(text, k))
