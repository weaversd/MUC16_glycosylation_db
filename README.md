# MUC16_glycosylation_db
creation of fasta files for MUC16glycosylation db search

to run:

`python O_linked_db_gen.py fasta_file.fasta glycan_list.txt`

and/or

`python N_linked_db_gen.py fasta_file.fasta glycan_list.txt`

where `fasta_file.fasta` is a fasta protein file of the protein(s) of interest
and `glycan_list.txt` is a list of glycans, one per line as described in: 


>Bollineni, R.C., Koehler, C.J., Gislefoss, R.E. et al. Large-scale intact glycopeptide identification by Mascot database search. Sci Rep 8, 2117 (2018). https://doi.org/10.1038/s41598-018-20331-2


The code was taken from the above citation, and modified slightly.
