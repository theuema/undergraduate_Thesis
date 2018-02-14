#!/bin/bash -

cat mypapers.bib > bibliography.bib
cat non_dblp.bib >> bibliography.bib

#sed -i 's/Lecture Notes in Computer Science/LNCS/' bibliography.bib
