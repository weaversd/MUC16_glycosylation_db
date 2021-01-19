# MUC16_glycosylation_db
creation of fasta files for MUC16glycosylation db search

One script for O linked and one for N linked.

to run:

`python O_linked_db_gen.py fasta_file.fasta glycan_list.txt`

and/or

`python N_linked_db_gen.py fasta_file.fasta glycan_list.txt`

where `fasta_file.fasta` is a fasta protein file of the protein(s) of interest
and `glycan_list.txt` is a list of glycans, one per line as described in: 

This will create a glyco_glyco fasta file with all the possible tryptic peptide/glycan combinations and a glycopeptide fasta file, with all of the same combinations combined by peptide.

>Bollineni, R.C., Koehler, C.J., Gislefoss, R.E. et al. Large-scale intact glycopeptide identification by Mascot database search. Sci Rep 8, 2117 (2018). https://doi.org/10.1038/s41598-018-20331-2


The code was taken from the above citation, translated to python3, and updated to work better with MUC16 specifically.
