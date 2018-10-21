
#!/usr/bin/env python3

import re

# Calculate nt composition for each sequence

genes = {}
with open('Python_08.fasta','r') as fasta:
 for line in fasta:
  line = line.rstrip()
  match = re.search(r'(^>\S+\s.*)', line)
  else:
   match = re.search(r'(^\w+$)', line) 

# genes[gene_id] = seq

print(genes)
