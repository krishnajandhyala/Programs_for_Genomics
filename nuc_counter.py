file = input("Enter your file path\t:\t")
string = open(file).readline()

A = string.count("A")
C = string.count("C")
G = string.count("G")
T = string.count("T")
total = A+C+G+T
print("A -",A,"\nC -",C,"\nG -",G,"\nT -",T,"\nTotal -",total)
