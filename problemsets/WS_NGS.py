#!/usr/bin/env python3

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO
#for seq_record in SeqIO.parse('./human_cds.fasta' , 'fasta'):
# print('ID',seq_record.id)
# print('Sequence',str(seq_record.seq))
# print('Length',len(seq_record))

#or:

id_dict = SeqIO.to_dict(SeqIO.parse('./human_cds.fasta' , 'fasta'))

len(id_dict)
list(id_dict.keys())

 for seq_record in SeqIO.parse('./human_cds.fasta', 'fasta'):

count_what = ['A', 'T', 'C', 'G']
for s in seq:
 name = s
 seq = seqs[s]
 print (s)
 for cw in count_what:
  print (cw, seq.count(cw))

print('As=', A_count[0], 'Ts=', T_count[1], 'Cs=', C_count[2], 'Gs=', G_count[3])


