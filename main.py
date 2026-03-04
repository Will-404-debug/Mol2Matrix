from utils.fasta_parser import read_fasta
from src.sequence_analysis import translate_dna


fasta_file = "data/fasta/test.fasta"

sequences = read_fasta(fasta_file)


for seq in sequences:

    protein = translate_dna(seq["sequence"])

    print("ID:", seq["id"])
    print("DNA :", seq["sequence"])
    print("Protein :", protein)