from pathlib import Path
import unittest

from src.sequence_analysis import translate_dna
from utils.fasta_parser import read_fasta


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TEST_FASTA = PROJECT_ROOT / "data" / "fasta" / "test.fasta"


class SequencePipelineTests(unittest.TestCase):
    def test_read_fasta_returns_expected_records(self):
        sequences = read_fasta(TEST_FASTA)

        self.assertEqual(len(sequences), 2)
        self.assertEqual(sequences[0]["id"], "example_sequence_1")
        self.assertEqual(sequences[1]["sequence"], "ATGAAATTTGGGCCCTAA")

    def test_translate_dna_returns_expected_protein(self):
        protein = translate_dna("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

        self.assertEqual(protein, "MAIVMGR")


if __name__ == "__main__":
    unittest.main()
