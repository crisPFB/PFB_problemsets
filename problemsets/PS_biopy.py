#!/usr/bin/env python3
import Bio.Seq
import re
from Bio.Alphabet import DNAAlphabet
from Bio import SeqIO

# just testing
seqobj = Bio.Seq.Seq('atgcgaggact')
seq_str = str(seqobj) #convert to string with str(seqobj)
print('{} has {} mucleotides'.format( seq_str , len(seq_str)))

#parsing
for seq_record in SeqIO.parse ('Python_08.fasta', 'fasta'):
    print('ID', seq_record.id)
    print('Sequence', str(seq_record.seq))
    print ('Length', len(seq_record))

#number of sequences
from seq_record in SeqIO.parse('Python_08.fasta', 'fasta'):
 import 
