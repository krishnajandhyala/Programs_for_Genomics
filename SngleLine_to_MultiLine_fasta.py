import argparse

parser = argparse.ArgumentParser(description='Convert multi fasta file with single lines to multiple lines')
parser.add_argument('input_file', help='Name of the input file')
parser.add_argument('output_file', help='Name of the output file')
parser.add_argument('-l', '--line_length', type=int, default=80, help='Length of the lines in the output file')
args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file
line_length = args.line_length

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
 for line in infile:
  if line[0] == '>':
   outfile.write(line)
  else:
   for i in range(0, len(line), line_length):
    outfile.write(line[i:i+line_length] + '\n')