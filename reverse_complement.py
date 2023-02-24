with open(input("Enter fasta file path \t:\t"), "r") as f:
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
with open("output.fasta", "w") as f:
    for header, sequence in sequences.items():
        comp1 = sequence.replace("A","I").replace("G","J")
        comp2 = comp1.replace("C","G").replace("T","A")
        comp3 = comp2.replace("I","T").replace("J","C")
        reversecomplement = comp3[::-1]
        f.write(">" + header + "\n")
        for i in range(0, len(comp3), 100):
            f.write(comp3[i:i+100] + "\n")

