# Find the reverse  complement of a DNA string
__author__ = 'Abdelrahman Hosny <abdelrahman.hosny@ieee.org>'


def reversecomplement(dna):
    reverse = ''
    for char in dna:
        if char == 'A':
            reverse += 'T'
        elif char == 'T':
            reverse += 'A'
        elif char == 'G':
            reverse += 'C'
        else:
            reverse += 'G'
    return reverse[::-1]

with open('rosalind_ba1c.txt', 'r') as file:
    text = file.readline().strip()
    with open('result.txt', 'w') as result:
        result.writelines(reversecomplement(text))