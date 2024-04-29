# Complementary DNA (7th Kyu)
# Your function receives one side of the DNA, you need to return the other complementary side.

# Solution One
def DNA_strand(dna):
    complement = ''
    for x in dna:
        if x == 'A':
            complement += 'T'
        elif x == 'T':
            complement += 'A'
        elif x == 'C':
            complement += 'G'
        elif x == 'G':
            complement += 'C'
    return complement

# Solution Two
def DNA_strand(dna):
    dict = {'A':'T','T':'A','C':'G','G':'C'}
    swap = ''.join(dict[x] for x in dna)
    return swap

# Community Solution
import string
def DNA_strand(dna):
    return dna.translate(string.maketrans('ATCG', 'TAGC'))
