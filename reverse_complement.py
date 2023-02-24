#Usage: python3 reverse_complement.py > output_RC.fasta

with open(input("Enter multifasta file path\t:\t")) as f:
    for line in f:
        if line.startswith(">"):
            print(line.strip())
        else:
            comp1 = line.replace("A","I").replace("G","J")
            comp2 = comp1.replace("C","G").replace("T","A")
            comp3 = comp2.replace("I","T").replace("J","C")
            reversecomplement = comp3[::-1]
            print(reversecomplement)
