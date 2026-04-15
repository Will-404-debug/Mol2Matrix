# Contributing

## Branching Model

- `main` is the stable branch.
- `develop` is the integration branch for validated work.
- Create feature branches from `develop`.
- Use focused branch names such as `feature/structure-analysis`, `fix/fasta-validation`, or `chore/project-hygiene`.

## Commit Convention

Use Conventional Commits:

- `feat: add PDB parser`
- `fix: reject invalid FASTA characters`
- `docs: clarify current project scope`
- `test: add translation unit tests`
- `refactor: separate CLI from analysis logic`
- `chore: update repository hygiene`

Keep commits small and single-purpose. Do not mix unrelated refactors, docs, and features in one commit unless they are tightly coupled.

## Pull Request Expectations

- Open branches against `develop` unless preparing a release or hotfix.
- Describe the scientific or technical purpose of the change.
- Include a short verification note with the commands run.
- Update documentation when behavior or project structure changes.

## Project Structure

Current implementation:

- `main.py` runs the minimal sequence analysis pipeline.
- `utils/fasta_parser.py` reads FASTA files.
- `src/sequence_analysis.py` translates DNA into protein.

Planned modules should be added on dedicated feature branches and documented in `README.md` when introduced.
