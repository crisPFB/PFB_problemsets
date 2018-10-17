#!/usr/bin/env python3

import sys

dna = sys.argv[1]

countAs = (dna.count ('A') + dna.count ('a'))
countTs = (dna.count ('T') + dna.count ('t'))
countCs = (dna.count ('C') + dna.count ('c'))
countGs = (dna.count ('G') + dna.count ('g'))

string = "My DNA content :{} is the count of As, {} is the count of Ts, {} is the count of Cs and {} is the count of Gs."
string.format(countAs, countTs, countCs, countGs)
new_string = string.format(countAs, countTs, countCs, countGs)

print(new_string)
