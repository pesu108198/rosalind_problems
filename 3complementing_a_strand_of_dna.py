dna = input().strip()

complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

reverse_complement = ''.join(complement[base] for base in reversed(dna) )
print(reverse_complement)
# st = "GATGGAACTTGACTACGTAAATT"

# str = str.maketrans("ATGC", "TACG")
# result = st[::-1].translate(str)
# print(result)
