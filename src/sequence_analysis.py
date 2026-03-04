from Bio.Seq import Seq


def translate_dna(dna_sequence):
    """
    Translate a DNA sequence into a protein sequence.
    """

    seq = Seq(dna_sequence)

    protein = seq.translate(to_stop=True)

    return str(protein)