seq_id = ""
seq_length = 0
with open("test.fasta", "r") as file:
    for line in file:
        if line.startswith(">"):
            if seq_id:
                print(f"Sequence ID: {seq_id}\tSequence Length: {seq_length}")
            seq_id = line[1:].strip()
            seq_length = 0

        else:
            seq_length += len(line.strip())
print(f"Sequence ID: {seq_id}\tSequence Length: {seq_length}")