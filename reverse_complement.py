file = input("Enter the file path \t:\t")
string = open(file).readline()
comp1 = string.replace("A","I").replace("G","J")
comp2 = comp1.replace("C","G").replace("T","A")
comp3 = comp2.replace("I","T").replace("J","C")
reversecomplement = comp3[::-1]
print(reversecomplement)