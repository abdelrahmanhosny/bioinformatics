from bm_preproc import BoyerMoore
from kmer_index import Index, SubseqIndex

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

def naive_with_counts(p, t):
    occurrences = []
    comparisons = 0
    alignments = 0
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        alignments += 1
        match = True
        for j in range(len(p)):  # loop over characters
            comparisons += 1
            if t[i+j] != p[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences, alignments, comparisons


def boyer_moore_with_counts(p, p_bm, t):
    """ Do Boyer-Moore matching. p=pattern, t=text,
        p_bm=BoyerMoore object for p """
    i = 0
    occurrences = []
    comparisons = 0
    alignments = 0
    while i < len(t) - len(p) + 1:
        alignments += 1
        shift = 1
        mismatched = False
        for j in range(len(p)-1, -1, -1):
            comparisons += 1
            if p[j] != t[i+j]:
                skip_bc = p_bm.bad_character_rule(j, t[i+j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                break
        if not mismatched:
            occurrences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)
        i += shift
    return occurrences, alignments, comparisons


genome = readGenome('chr1.GRCh38.excerpt.fasta')
p = 'GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG'
occurrences, num_alignments, num_character_comparisons = naive_with_counts(p, genome)
print(occurrences, num_alignments, num_character_comparisons)
print ''

p_bm = BoyerMoore(p, alphabet='ACGT')
occurrences, num_alignments, num_character_comparisons = boyer_moore_with_counts(p, p_bm, genome)
print(occurrences, num_alignments, num_character_comparisons)
print ''

def approximate_match(p, t, n):

    segment_length = int(round(len(p) / (n+1)))
    all_matches = set()

    total_hits = 0

    for i in range(n+1):
        start = int(i*segment_length)
        end = min((i+1)*segment_length, len(p))
        p_bm = BoyerMoore(p[start:end], alphabet='ACGT')
        matches, aligns, comps = boyer_moore_with_counts(p[start:end], p_bm, t)
        total_hits += len(matches)

        for m in matches:
            if m < start or m-start+len(p) > len(t):
                continue

            mismatches = 0
            for j in range(0, start):
                if not p[j] == t[m-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break

            for j in range(end, len(p)):
                if not p[j] == t[m-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break

            if mismatches <= n:
                all_matches.add(m - start)

    return list(all_matches), total_hits

def approximate_match_index(p, index, t):

    n = 2
    segment_length = int(round(len(p) / (n+1)))
    all_matches = set()

    total_hits = 0

    for i in range(n+1):
        start = int(i*segment_length)
        end = min((i+1)*segment_length, len(p))

        matches = index.query(p[start:end])
        total_hits += len(matches)

        for m in matches:
            if m < start or m-start+len(p) > len(t):
                continue

            mismatches = 0
            for j in range(0, start):
                if not p[j] == t[m-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break

            for j in range(end, len(p)):
                if not p[j] == t[m-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break

            if mismatches <= n:
                all_matches.add(m - start)

    return list(all_matches), total_hits

def approximate_match_seubseq_index(p, index, t):

    n = 2
    segment_length = int(round(len(p) / (n+1)))
    all_matches = set()

    total_hits = 0

    for i in range(n+1):
        start = int(i*segment_length)
        end = min((i+1)*segment_length, len(p))

        matches = index.query(p[start:])
        matches.extend(index.query(p[start+1:]))
        matches.extend(index.query(p[start+2:]))
        total_hits += len(matches)

        for m in matches:
            if m < start or m-start+len(p) > len(t):
                continue

            mismatches = 0
            for j in range(0, start):
                if not p[j] == t[m-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break

            for j in range(end, len(p)):
                if not p[j] == t[m-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break

            if mismatches <= n:
                all_matches.add(m - start)

    return list(all_matches), total_hits

p = 'GGCGCGGTGGCTCACGCCTGTAAT'
#print len(approximate_match(p, genome, 2)[0])
#print approximate_match(p, genome, 2)[1]

index8 = Index(genome, 8)
#print len(approximate_match_index(p, index8, genome)[0])
#print approximate_match_index(p, index8, genome)[1]



ind = SubseqIndex(genome, 8, 3)
print approximate_match_seubseq_index(p, ind, genome)[0]
print approximate_match_seubseq_index(p, ind, genome)[1]
