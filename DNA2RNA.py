#Usage python3 DNA2RNA.py > output_RNA.fasta

with open(input("Enter Multifasta file path\t:\t"), "r") as f:
    for line in f:
        if line.startswith(">"):
            print(line.strip())
        else:
            rna_sequence = line.strip().replace("T", "U")
            print(rna_sequence)
