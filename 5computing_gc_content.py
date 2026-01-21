# ==============================================================================
# COMPLETE STEP-BY-STEP EXPLANATION OF DNA GC-CONTENT CALCULATOR
# ==============================================================================

# ------------------------------------------------------------------------------
# FUNCTION 1: calculate_gc_content
# Purpose: Calculate what percentage of a DNA string is made of G and C bases
# ------------------------------------------------------------------------------

def calculate_gc_content(dna_string):
    
    if len(dna_string) == 0:
        return 0.0
   
    gc_count = dna_string.count('G') + dna_string.count('C')
   
    
    return (gc_count / len(dna_string)) * 100
   
# ------------------------------------------------------------------------------
# FUNCTION 2: parse_fasta
# Purpose: Read FASTA format and organize it into a dictionary
# FASTA format example:
#   >SequenceID
#   ATCGATCG
#   GGCCTTAA
# ------------------------------------------------------------------------------

def parse_fasta(fasta_text):
    #creating initial storage 
    sequences = {}
    current_id = None
    current_sequence = []


    #running the loop i.e. assigining values to out storage
    for line in fasta_text.strip().split('\n'):
        line = line.strip()

        
        if line.startswith('>'):
            #saving the previous and moving to next
            if current_id:
             
                sequences[current_id] = ''.join(current_sequence)
          
            current_id = line[1:]
    
            
            current_sequence = []
            
            
        else:
      #if no new line it must be the part of the previous line.
            current_sequence.append(line)
            

    #For the last round of the loop we'll have to manually write code as there is no further line to
    #to activate the saving of the previous line
    if current_id:

        
        sequences[current_id] = ''.join(current_sequence)
     
    
    return sequences
 
# ------------------------------------------------------------------------------
# FUNCTION 3: find_highest_gc_content
# Purpose: Compare all sequences and find which has highest GC percentage
# ------------------------------------------------------------------------------

def find_highest_gc_content(fasta_text):
    
    sequences = parse_fasta(fasta_text)
    max_gc = 0
    max_id = None
    for seq_id, sequence in sequences.items():
        gc_content = calculate_gc_content(sequence)
        if gc_content > max_gc:
            
            max_gc = gc_content
            
            
            max_id = seq_id
    return max_id, max_gc


# ------------------------------------------------------------------------------
# MAIN EXECUTION: Using the functions
# ------------------------------------------------------------------------------

sample_input = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""

max_id, seq_id = find_highest_gc_content(sample_input)
print(max_id, seq_id)