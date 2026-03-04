from utils.fasta_parser import read_fasta

fasta_file = "data/fasta/test.fasta"

sequences = read_fasta(fasta_file)

for seq in sequences:
    print("ID:", seq["id"])
    print("Sequence:", seq["sequence"])