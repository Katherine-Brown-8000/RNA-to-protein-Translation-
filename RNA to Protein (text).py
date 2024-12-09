# RNA to Protein

sequence = "CACAUAUAG"

def translation(sequence, codons):
    amino_acids = []                        # store the amino acids in a list
    for i in range(0, len(sequence), 3):    # read the sequence in triplets
        codon = sequence[i:i+3]             # get a codon
        amino_acid = codons.get(codon, "")  # get corresponding amino acid
        if amino_acid == " ":               # check for stop codon
            break
        amino_acids.append(amino_acid)      # Add amino acid to list
    return "".join(amino_acids)             # Join and return as protein


codons = {
    "AUG": "M", # The universal start codon
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUU": "I", "AUC": "I", "AUA": "I",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UAU": "Y", "UAC": "Y",
    "CAU": "H", "CAC": "H",
    "CAA": "Q", "CAG": "Q",
    "AAU": "N", "AAC": "N",
    "AAA": "K", "AAG": "K",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UGU": "C", "UGC": "C",
    "UGG": "W",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "UAA": " ", "UAG": " ", "UGA": " ", # the stop codons
}

result = translation(sequence, codons)
print(result)
