# dna_string = "AGCTTTTCATTCTGACTGCAACGGCACATATGTCTCTGTGTGGATTTAAAAAAAGAGTCTCTGATAGCAGC"

# count_a = 0
# count_t = 0
# count_g = 0
# count_c = 0

# for nucleotide in dna_string:
#     if nucleotide == 'A':
#         count_a += 1
#     elif nucleotide == 'T':
#         count_t += 1
#     elif nucleotide == 'G':
#         count_g += 1
#     elif nucleotide == 'C': 
#         count_c += 1
# print (f"{count_a} {count_t} {count_g} {count_c} ") 
count = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
count_1 = count.count("A")
count_2 = count.count("T")
count_3 = count.count("G")
count_4 = count.count("C")
print(f"{count_1}, {count_2}, {count_3}, {count_4}")