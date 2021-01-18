import os
import sys
import re
from pyteomics import fasta, parser

def transformFasta(fastafile,glycofile):

    #read the fils to marry
    glycos = read_glyco(glycofile)
    proteins = list(fasta.read(fastafile))

    #open new fastafiles
    proteinlevel_fasta = open('Glyco_prot_%s' %(fastafile),'w')
    peptidelevel_fasta = open('Glyco_pep_%s' %(fastafile),'w')
    glycolevel_fasta = open('Glyco_glyco_%s' %(fastafile),'w')


    #counters
    procounter = 0
    pepcounter = 0



    for protein in proteins:
        proteinlevel_sequences = ''
        pep_appendix = 1

        prot, seq = protein
        acc,ident,descr = splitter(prot)
        
        procounter +=1
        if procounter%1000==0:
            print('----> Process protein %s:%s' %(procounter,ident))

        peptides = parser.cleave(seq,parser.expasy_rules['trypsin'], missed_cleavages=0, min_length=5)


        for pep in peptides:
            if len(pep) < 30:
                peptidelevel_sequences = ''
                glyco_appendix = 1

                pepcounter+=1
                if pepcounter%10000==0:
                    print('Process peptide %s' %pepcounter)
                
                if re.search('N.[TSC]', pep): # find the pattern NxT, NxS or NxC in the peptide
                    #peptides_motiv.append(pep)
                    for glyco in glycos:

                        #adding the peptides to the sequences
                        proteinlevel_sequences += '%s%s' %(glyco,pep)
                        peptidelevel_sequences += '%s%s' %(glyco,pep)
                        #for the glycolevel sequence, we can write it right away
                        glycolevel_fasta.write('>sp|%s_%s_%s|%s %s\n' %(acc,str(pep_appendix),str(glyco_appendix),ident,descr))
                        
                        glycolevel_fasta.write('%s%s\n' %(glyco,pep))
                        glyco_appendix +=1

                    #for the peptidelevel_sequences we write the fasta
                    peptidelevel_sequences = insert_newlines(peptidelevel_sequences)
                    peptidelevel_fasta.write('>sp|%s_%s|%s %s\n' %(acc,str(pep_appendix),ident,descr)),
                    peptidelevel_fasta.write('%s\n' %(peptidelevel_sequences))
                    pep_appendix +=1

                if proteinlevel_sequences:   
                    #for the proteinlevel_sequences we write the fasta 
                    proteinlevel_sequences = insert_newlines(proteinlevel_sequences)
                    proteinlevel_fasta.write('>sp|%s|%s %s\n' %(acc,ident,descr))
                    proteinlevel_fasta.write('%s\n' %(proteinlevel_sequences))

    #closing the new files
    glycolevel_fasta.close()      
    peptidelevel_fasta.close() 
    proteinlevel_fasta.close()  
    print('Done')


def read_glyco(glycofile): 
    ''' reads a .txt file with glyco sequences and returns a list of glyco sequences'''
    glycos = open(glycofile,'r').readlines()
    return [i.strip() for i in glycos]

def insert_newlines(string, every=64):
    return '\n'.join(string[i:i+every] for i in range(0, len(string), every))

def splitter(p):
    start = p.find('|')
    middle = p.find('|',start+1)
    middle2 = p.find(' ',middle+1)
    end = p.find('OS=')
    return p[start+1:middle],p[middle+1:middle2], p[middle2+1:end].strip()



if __name__ == '__main__':

    if len(sys.argv) <3:
        print('\n***************************************************\n\
            Use as follows:')
        print('"Generate_Glycodb.py fastafile.fasta glycofile.txt"\
            \n***************************************************\n')
    else:
        transformFasta(sys.argv[1],sys.argv[2])  
