#!/usr/bin/env python3
import Bio.Seq
seqobj = Bio.Seq.Seq('atgcgaggact')
seq_str = str(seqobj) #convert to strin with str(seqobj)
print('{} has {} mucleotides'.format( seq_str , len(seq_str)))
