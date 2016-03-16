# count the number of times a pattern appears in a text
__author__ = 'Abdelrahman Hosny <abdelrahman.hosny@ieee.org>'


def patterncount(text, pattern):
    count = 0
    for i in range(0, len(text)-len(pattern)):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

with open('rosalind_ba1a.txt', 'r') as file:
    text = file.readline().strip()
    pattern = file.readline().strip()
    print text
    print pattern
    print patterncount(text, pattern)