#file = input("Enter your file path\t:\t")
#string = open(file).readlines()

#A = string.count("A")
#C = string.count("C")
#G = string.count("G")
#T = string.count("T")
#total = A+C+G+T
#print("A -",A,"\nC -",C,"\nG -",G,"\nT -",T,"\nTotal -",total)


import re

A=T=G=C=N=0

with open(input("Give your file name/path \t:\t")) as fh:
	#header = re.findall(">", fh)
	for line in fh:
		A += line.count("A")
		T += line.count("T")
		G += line.count("G")
		C += line.count("C")
		N += line.count("N")
	total = A+T+G+C+N

print("A -",A,"\nC -",C,"\nG -",G,"\nT -",T,"\nN -",N,"\nTotal -",total)

