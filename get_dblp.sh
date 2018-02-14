#!/bin/bash -

rm -f tmp_urls.txt

find . -iname "*.tex" -exec grep -Eio "DBLP:[^}]*" {} \; | while read line
do
  arr=$(echo $line | tr "," "\n")

  for a in $arr
  do
    entry=$(echo $a | tr -d '[:space:]');
    if [[ $entry == DBLP* ]]; then
      # if entry does not exist in final bibliography.bib -> prepare for download
      #exists=$(grep -c "$entry" bibliography.bib);
      exists=$(grep -c "$entry" dblp.bib);
      if [[ $exists == 0 ]]; then
        echo "$entry"
  	conf=$(echo $entry | sed 's/^DBLP://');
        url="http://dblp2.uni-trier.de/rec/bib2/$conf.bib"
        #url="http://dblp2.uni-trier.de/rec/bib0/$conf.bib"
        echo $url >> tmp_urls.txt
      fi
    fi
  done
done

if [ -f tmp_urls.txt ]; then
  cat tmp_urls.txt | sort -u | while read url
  do
    wget -O tmp.bib --user-agent="Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008092416 Firefox/3.0.3" $url
    cat tmp.bib >> dblp.bib
  done
fi

python3 dblp.py

# changed copy process #
#./copy_bib.sh
#cat dblp.bib > bibliography.bib
cat mypapers.bib > bibliography.bib
cat non_dblp.bib >> bibliography.bib

#sed -i 's/Lecture Notes in Computer Science/LNCS/' bibliography.bib
