file = input("Enter your file name here :   ")
openfile = open(file)
dna = openfile.readline()
rna = dna.replace("T","U")
print(rna)