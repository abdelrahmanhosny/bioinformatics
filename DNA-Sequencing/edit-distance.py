from collections import defaultdict

dct = defaultdict(list)
def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()  # skip name line
            seq = fh.readline().rstrip()  # read base sequence
            fh.readline()  # skip placeholder line
            qual = fh.readline().rstrip() # base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences

def editDistance(x, y):
    # Create distance matrix
    D = []
    for i in range(len(x)+1):
        D.append([0]*(len(y)+1))
    # Initialize first row and column of matrix
    for i in range(len(x)+1):
        D[i][0] = i
    for i in range(len(y)+1):
        D[0][i] = 0
    # Fill in the rest of the matrix
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            distHor = D[i][j-1] + 1
            distVer = D[i-1][j] + 1
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1
            D[i][j] = min(distHor, distVer, distDiag)
    # Edit distance is the value in the bottom right corner of the matrix
    return min(D[-1][1:])

def overlap(a, b, min_length):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's prefix in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match

# genome = readGenome('chr1.GRCh38.excerpt.fasta')
# t = genome
# p = 'GATTTACCAGATTGAG'
#print editDistance(p, t)

def overlap_all_pairs(reads, k):
    kmer_dict = defaultdict(set)
    for read in reads:
        for i in range(0, len(read) - k + 1):
            kmer_dict[read[i:i+k]].add(read)

    overlap_graph = []
    for read in reads:
        suffix = read[-k:]
        possible_overlap_reads = list(kmer_dict[suffix])
        for possible_overlap in possible_overlap_reads:
            if read != possible_overlap:
                length = overlap(read, possible_overlap, k)
                if length > 0:
                    overlap_graph.append((read, possible_overlap))
    return overlap_graph

reads = readFastq('ERR266411_1.for_asm.fastq')
# reads = ['CGTACG', 'TACGTA', 'GTACGT', 'ACGTAC', 'GTACGA', 'TACGAT']
graph = overlap_all_pairs(reads, 30)
nodes = set()
for edge in graph:
    nodes.add(edge[0])
print len(graph)
print len(list(nodes))


