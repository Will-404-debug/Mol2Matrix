from pathlib import Path

from src.sequence_analysis import translate_dna
from utils.fasta_parser import read_fasta


def main():
    fasta_file = Path(__file__).resolve().parent / "data" / "fasta" / "test.fasta"
    sequences = read_fasta(fasta_file)

    for sequence in sequences:
        protein = translate_dna(sequence["sequence"])
        print("ID:", sequence["id"])
        print("DNA :", sequence["sequence"])
        print("Protein :", protein)


if __name__ == "__main__":
    main()
