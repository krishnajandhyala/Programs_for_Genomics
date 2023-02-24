##Usage: python3 nuc_counter.py > output_num.txt
A=T=G=C=N=0

with open(input("Enter fasta file path \t:\t"), "r") as f:
        for line in f:
                if line.startswith(">"):
                    print
                else:
                    A += line.count("A")
                    T += line.count("T")
                    G += line.count("G")
                    C += line.count("C")
                    N += line.count("N")
                    total = A+T+G+C+N
print("A -",A,"\nC -",C,"\nG -",G,"\nT -",T,"\nN -",N,"\nTotal -",total)
