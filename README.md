# Mol2Matrix

Mol2Matrix is a bioinformatics project intended to explore the relationship between:

genetic sequence -> protein structure -> molecular interactions -> conceptual biomaterial matrix parameters.

The project follows a structural bioinformatics approach applied to tissue engineering concepts.

---

# Project Objective

The goal is to develop a computational pipeline capable of:

- analyzing biological sequences
- visualizing and comparing protein structures
- analyzing molecular interactions
- integrating conceptual parameters related to biomaterial matrices

This project explores the connection between structural bioinformatics and biomaterial engineering.

---

# Current Status

The repository is currently at an early implementation stage.

Implemented today:

- FASTA parsing through `utils/fasta_parser.py`
- DNA to protein translation through `src/sequence_analysis.py`
- a minimal command-line entrypoint in `main.py`

Planned but not yet implemented:

- structural analysis modules
- interaction analysis modules
- biomaterial matrix modeling modules
- tests and example datasets

---

# Planned Features

## Sequence Analysis

- FASTA file reading
- simple sequence alignment
- mutation detection
- DNA -> protein translation

## Structural Analysis

- PDB file import
- extraction of atomic coordinates
- identification of secondary structures (alpha-helices, beta-sheets)
- comparison of protein structures

## Interaction Analysis

- interatomic distance calculation
- simplified hydrogen bond detection
- identification of critical residues

## Conceptual Biomaterial Matrix Modeling

- biomaterial parameterization
- crosslinking density
- fibrillar organization
- theoretical stability

---

# Target Project Architecture

```text
mol2matrix/
|-- data/
|   |-- fasta/
|   `-- pdb/
|-- src/
|   |-- sequence_analysis.py
|   |-- structure_analysis.py
|   |-- interaction_analysis.py
|   `-- matrix_model.py
|-- utils/
|   |-- fasta_parser.py
|   `-- pdb_parser.py
|-- results/
|-- tests/
|-- main.py
|-- requirements.txt
`-- README.md
```

The current repository does not yet contain all of the modules shown above. This tree represents the intended architecture.

---

# Technologies

Main language:

- Python

Key libraries:

- Biopython
- MDAnalysis
- NumPy
- Pandas
- Matplotlib

---

# Installation

Create a Python environment:

```bash
python -m venv mol2matrix-env
source mol2matrix-env/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv mol2matrix-env
.\mol2matrix-env\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Data Sources

The project relies on publicly available biological data:

- Protein Data Bank (PDB)
- FASTA sequence databases

---

# Scientific Pipeline

The Mol2Matrix pipeline follows four main stages:

1. Biological sequence analysis
2. Protein structural analysis
3. Molecular interaction analysis
4. Conceptual biomaterial parameter modeling

At the moment, only stage 1 is partially implemented in code.

---

# Project Deliverables

- documented source code
- reproducible pipeline
- test dataset
- scientific report (~20-30 pages)
- functional demonstration

---

# Author

William Guilon Dronnier

Project developed within the context of structural bioinformatics research.
