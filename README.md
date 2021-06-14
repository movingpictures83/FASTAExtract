# FASTAExtract
# Language: Python
# Input: TXT (keyword-value pairs)
# Output: FASTA
# Tested with: PluMA 1.1, Python 3.6
# Dependency:

PluMA plugin that extracts a portion of a sequence from a FASTA file.

The plugin accepts as input a tab-delimited TXT file of keyword-value pairs.  Keywords:

fasta: FASTA file of sequence
start: Start nucleotide
end: End nucleotide

Output region of sequence will be in FASTA format as well.
