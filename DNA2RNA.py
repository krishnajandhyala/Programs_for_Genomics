with open(input("Enter the path of the multifasta file \t:\t"), "r") as f:
    sequences = {}
    current_sequence = ""
    for line in f:
        if line.startswith(">"):
            if current_sequence:
                sequences[header] = current_sequence
            header = line.strip()[1:]
            current_sequence = ""
        else:
            current_sequence += line.strip()
    sequences[header] = current_sequence
with open("output_DNA2RNA.fasta", "w") as f:
    for header, sequence in sequences.items():
        rna_sequence = sequence.replace("T", "U")
        f.write(">" + header + "\n")
        for i in range(0, len(rna_sequence), 100):
            f.write(rna_sequence[i:i+100] + "\n")
