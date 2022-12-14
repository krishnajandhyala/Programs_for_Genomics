import argparse

my_parser = argparse.ArgumentParser(description="Trim ends from fasta sequence",add_help=False)
main_group = my_parser.add_argument_group('Main options')
main_group.add_argument('-i',"--input", help="Input Fasta file", required=True)
main_group.add_argument("-o","--output", help="Outputs Trimmed Fasta file", required=True)
help_args = my_parser.add_argument_group('Help')
help_args.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='Show this help message and exit')

args = my_parser.parse_args()

filename = args.input
outfile = args.output
out = open(outfile,'w')
with open(filename) as fh:
    seq = ''
    header = fh.readline()
    for line in fh:
        seq += line.strip()
    trim_seq = seq[31:29860]
    print(f'{header}{trim_seq}', file = out)
    
