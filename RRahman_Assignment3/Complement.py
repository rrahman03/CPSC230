# this method loops through DNA sequence + checks for complement + appends to output
def complement(dna_sequence): 
    new_dna = " "
    # returning the complement
    for letter in dna_sequence: 
        if letter == "A":
            new_dna += "T"
        elif letter == "T":
            new_dna += "A"
        elif letter == "G":
            new_dna += "C"
        elif letter == "C":
            new_dna += "G"
    return new_dna 

# returns the sequence backwards, calling the DNA sequence method and flipping the return
def rev_complement(dna_sequence):
    # reversing the input 
    rev_sequence = dna_sequence[::-1] 
     # calling complement
    return complement(rev_sequence)

# asking user for input
dna_sequence = input("Enter a DNA sequence (A, C, G, T): ") 

# keeps program going incase user puts incorrect format for input
keep_going = True 
while keep_going:
    for letter in dna_sequence:
        if letter not in ["A", "C", "G", "T"]:
            # continues to prompt user for correct input
            print("Enter the correct sequence of letters: ") 
            dna_sequence = input("Enter a DNA sequence (A, C, G, T): ")
            keep_going = True 
            break
        else:
            keep_going = False

# prints the user's inputted DNA sequence
print(complement(dna_sequence))
# reverses the user's inputted DNA sequence
print(rev_complement(dna_sequence))