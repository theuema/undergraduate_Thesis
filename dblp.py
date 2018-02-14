#!/usr/bin/env python3

import re
import shutil
import os.path

import collections
from collections import Counter
from urllib.request import urlopen, urlretrieve
from urllib.error import URLError, HTTPError

booktitle = {
  'acisp'       : 'Information Security and Privacy -- {ACISP}', 
  'acns'        : 'Applied Cryptography and Network Security -- {ACNS}', 
  'acsac'       : 'Annual Computer Security Applications Conference -- {ACSAC}',
  'africacrypt' : 'Progress in Cryptology -- {AFRICACRYPT}',
  'asia'        : 'Asia Conference on Computer and Communications Security -- {AsiaCCS}', 
  'asiacrypt'   : 'Advances in Cryptology -- {ASIACRYPT}', 
  'asplos'      : 'Architectural Support for Programming Languages and Operating Systems -- {ASPLOS}',
  'buildsys'    : 'Embedded Systems for Energy-Efficient Built Environments -- {BuildSys}',
  'cans'        : 'Cryptology and Network Security -- {CANS}', 
  'cardis'      : 'Smart Card Research and Advanced Applications -- {CARDIS}',
  'cav'         : 'Computer Aided Verification -- {CAV}',
  'cc'          : 'Compiler Construction -- {CC}',
  'ccnc'        : 'Consumer Communications {\&} Networking Conference -- {CCNC}',
  'ccs'         : 'Conference on Computer and Communications Security -- {CCS}',
  'ccsw'        : 'Cloud Computing Security Workshop -- {CCSW}',
  'cns'         : 'Communications and Network Security -- {CNS}',
  'cscwd'       : 'Computer Supported Cooperative Work in Design -- {CSCWD}',
  'csfw'        : 'Computer Security Foundations -- {CSF}',
  'ches'        : 'Cryptographic Hardware and Embedded Systems -- {CHES}', 
  'chi'         : 'Conference on Human Factors in Computing Systems -- {CHI}',
  'codaspy'     : 'Conference on Data and Application Security and Privacy -- {CODASPY}',
  'comsnets'    : 'International Conference on Communication Systems and Networks -- {COMSNETS}',
  'comsware'    : 'Communication System Software and Middleware -- {COMSWARE}', 
  'corr'        : '', 
  'cosade'      : 'Constructive Side-Channel Analysis and Secure Design -- {COSADE}',
  'crypto'      : 'Advances in Cryptology -- {CRYPTO}', 
  'cs'          : 'Cryptography and Security in Computing Systems -- {CS2@HiPEAC}',
  'csaw'        : 'Computer Security Architecture Workshop -- {CSAW}',
  'cset'        : 'Cyber Security Experimentation and Test -- {CSET}',
  'ctrsa'       : 'Topics in Cryptology -- {CT-RSA}', 
  'date'        : 'Design, Automation {\&} Test in Europe -- {DATE}',
  'dbsec'       : 'Data and Applications Security and Privacy -- {DBSec}',
  'diau'        : 'Design Issues in Anonymity and Unobservability -- {DIAU}',
  'dimva'       : 'Detection of Intrusions and Malware {\&} Vulnerability Assessment -- {DIMVA}',
  'dpm'         : 'Data Privacy Management, and Security Assurance -- {DPM}',
  'dsd'         : 'Digital System Design -- {DSD}',
  'dsn'         : 'Dependable Systems and Networks -- {DSN}',
  'eurocrypt'   : 'Advances in Cryptology -- {EUROCRYPT}', 
  'eurosec'     : 'European Workshop on System Security -- {EUROSEC}',
  'eurosp'      : 'IEEE European Symposium on Security and Privacy -- {EURO S{\&}P}', 
  'esmart'      : 'Smart Card Programming and Security -- {E-smart}',
  'esorics'     : 'European Symposium on Research in Computer Security -- {ESORICS}',
  'essos'       : 'Engineering Secure Software and Systems -- {ESSoS}',
  'essderc'     : 'European Solid State Device Research Conference -- {ESSDERC}',
  'fc'          : 'Financial Cryptography -- {FC}',
  'fdtc'        : 'Fault Diagnosis and Tolerance in Cryptography -- {FDTC}',
  'fse'         : 'Fast Software Encryption -- {FSE}', 
  'hasp'        : 'Hardware and Architectural Support for Security and Privacy -- {HASP}', 
  'hotsec'      : '{USENIX} Workshop on Hot Topics in Security -- {HotSec}',
  'hpca'        : 'High Performance Computer Architecture -- {HPCA}', 
  'IEEEias'     : 'Information Assurance and Security -- {IAS}',
  'icassp'      : 'International Conference on Acoustics, Speech, and Signal Processing -- {ICASSP}',
  'host'        : 'Hardware Oriented Security and Trust -- {HOST}',
  'huc'         : 'Conference on Pervasive and Ubiquitous Computing -- {UbiComp}', 
  'icc'         : 'International Conference on Communications -- {ICC}',
  'icics'       : 'Information and Communications Security -- {ICICS}',
  'icisc'       : 'Information Security and Cryptology -- {ICISC}', 
  'icse'        : 'International Conference on Software Engineering -- {ICSE}',
  'IEEEares'    : 'Availability, Reliability and Security -- {ARES}',
  'ima'         : 'Cryptography and Coding -- {IMA}',
  'indocrypt'   : 'Progress in Cryptology -- {INDOCRYPT}', 
  'infocom'     : '{IEEE} {INFOCOM}',
  'internetware': 'Symposium of Internetware -- {Internetware}',
  'intrust'     : 'Conference on Trusted Systems -- {INTRUST}',
  'iotpts'      : 'Workshop on IoT Privacy, Trust, and Security -- {IoTPTS@AsiaCCS}', 
  'isca'        : 'International Symposium on Computer Architecture -- {ISCA}',
  'isw'         : 'Information Security -- {ISC}', 
  'iwsec'       : 'International Workshop on Security -- {IWSEC}',
  'iswc'        : 'International Symposium on Wearable Computers -- {ISWC}',
  'latincrypt'  : 'Progress in Cryptology -- {LATINCRYPT}',
  'ndss'        : 'Network and Distributed System Security Symposium -- {NDSS}', 
  'nips'        : 'Neural Information Processing Systems -- {NIPS}',
  'nsdi'        : 'Networked Systems Design and Implementation -- {NSDI}',
  'nss'         : 'Network and System Security -- {NSS}',
  'mobicom'     : 'Mobile Computing and Networking -- {MOBICOM}',
  'mobiheld'    : 'Workshop on Networking, Systems, and Applications for Mobile Handhelds -- {MobiHeld}',
  'mobisec'     : 'Security and Privacy in Mobile Information and Communication Systems -- {MOBISEC}',
  'mobiquitous' : 'Mobile and Ubiquitous Systems -- {MobiQuitous}',
  'mobisys'     : 'Mobile Systems -- {MobiSys}',
  'mswim'       : 'Symposium on QoS and Security for Wireless and Mobile Networks -- {Q2SWinet}',
  'mum'         : 'Mobile and Ubiquitous Multimedia -- {MUM}', 
  'pairing'     : 'Pairing-Based Cryptography -- {Pairing}',
  'pam'         : 'Passive and Active Measurement -- {PAM}',
  'pet'         : 'Privacy Enhancing Technologies -- {PET}',
  'percom'      : 'Pervasive Computing and Communication Workshops -- {PerCom}', 
  'pkc'         : 'Public Key Cryptography -- {PKC}',
  'pldi'        : 'Programming Language Design and Implementation -- {PLDI}',
  'popl'        : 'Principles of Programming Languages -- {POPL}',
  'raid'        : 'Recent Advances in Intrusion Detection -- {RAID}', 
  'sacrypt'     : 'Selected Areas in Cryptography -- {SAC}', 
  'sec'         : 'Information Security Conference -- {SEC}',
  'securecomm'  : 'Security and Privacy in Communication Networks -- {SecureComm}',
  'sensys'      : 'Conference on Embedded Network Sensor Systems -- {SenSys}',
  'scn'         : 'Security and Cryptography for Networks -- {SCN}',
  'soups'       : 'Symposium On Usable Privacy and Security -- {SOUPS}',
  'sp'          : '{IEEE} Symposium on Security and Privacy -- {S{\&}P}',
  'spsm'        : 'Security and Privacy in Smartphones {\&} Mobile Devices -- {SPSM@CCS}',
  'spw'         : 'Security Protocols Workshop -- {SPW}',
  'tacas'       : 'Tools and Algorithms for the Construction and Analysis of Systems -- {TACAS}',
  'trustcom'    : 'Trust, Security and Privacy in Computing and Communications -- {TrustCom}',
  'uic'         : 'Ubiquitous Intelligence and Computing -- {UIC}', 
  'usenix'      : '{USENIX} Annual Technical Conference -- {USENIX} {ATC}',
  'uss'         : '{USENIX} Security Symposium',
  'STOC22'        : 'Symposium on the Theory of Computing -- {STOC}',
  'trust'       : 'Trust and Trustworthy Computing -- {TRUST}',
  'vietcrypt'   : 'Progress in Cryptology -- {VIETCRYPT}',
#  'w'           : 'Financial Cryptography -- {FC}',
  'waifi'       : 'Arithmetic of Finite Fields -- {WAIFI}',
  'webapps'     : 'Web Application Development -- {WebApps}',
  'wifs'        : 'Workshop on Information Forensics and Security -- {WIFS}',
  'wisa'        : 'Information Security Applications -- {WISA}',
  'wisec'       : 'Security and Privacy in Wireless and Mobile Networks -- {WISEC}',
  'wistp'       : 'Information Security Theory and Practice -- {WISTP}',
  'wpes'        : 'Workshop on Privacy in the Electronic Society -- {WPES}',
  'wmcsa'       : 'Mobile Computing Systems and Applications -- {HotMobile}',
  'woot'        : 'Workshop on Offensive Technologies -- {WOOT}', 
}

entries = {
  #'proceedings'   : {'editor','title','series','volume','publisher','year','isbn'},
'proceedings'   : {'title','series','volume','publisher','isbn'},
  #'inproceedings' : {'author', 'title', 'pages', 'year', 'url', 'booktitle', 'publisher'},
 'inproceedings' : {'author', 'title', 'pages', 'year', 'booktitle', 'publisher'},  
  #'article'       :  {'author', 'title', 'journal', 'volume', 'pages', 'year', 'url'},
'article'       :  {'author', 'title', 'journal', 'volume', 'pages', 'year'},  
  'book' : {'author', 'title', 'series', 'publisher', 'year'}
}

def add_entry():
  if 'type' in myentry:
    # skip eprint
    #if not myentry['key'][:4] == 'iacr' and not myentry['key'][:8] == 'dagstuhl':
    ###mylist[myentry['key']] = myentry
    mylist.append(myentry)
    #if 'author' in myentry:
    #  myauthorlist.update(myentry['author'].split(' and '))

#mylist = {}
mylist = []
myauthorlist = Counter()
myentry = {}
t = '';

#http://dblp.uni-trier.de/pers/tb2/m/Mendel:Florian.bib

#try:
#  #urlretrieve('http://dblp.uni-trier.de/pers/tb2/m/Mendel:Florian.bib','Mendel_Florian.bib')
#  print('downloading Mendel_Florian.bib ... ok')
#except URLError as e:
#  print('downloading Mendel_Florian.bib ... failed')

fin = open('dblp.bib','r')
data = fin.readlines()

for line in data:
  line = line.strip()
  p = re.compile('@\w+')
  m = p.match(line)
  if m:
    t = '';
    k = line.split('/')
    add_entry()
    myentry = {}
    #myentry['key'] = (k[-2]+k[-1])[:-1]
    myentry['key'] = (line.split('{'))[1][:-1]
    myentry['type'] = m.group()[1:]
  else:
    t = t + ' ' + line;
    if (t.count('{') - t.count('}')) == 0:
      line = t.strip()
      t = ''
      val = line[line.index("{")+1:line.rindex("}")]
      p2 = re.compile('[a-z|A-Z]+')
      elem = p2.match(line).group()
      if elem == 'crossref':
        l1 = line.split('/')
        myentry['crossref'] = (line.split('{'))[1][:-2]
        ws = re.sub("^[0-9]*","",(l1[2])[:-2])
        if ws:
          if ws in booktitle:
            myentry['booktitle'] = (booktitle[ws])
          else:
            print ('warning: workshop ' + ws + ' not found ' + 'for entry ' + myentry['crossref']);
        elif l1[1] in booktitle:
          myentry['booktitle'] = (booktitle[l1[-2]] + ' ' + l1[-1][:4])
        else:
          print('warning: ' + l1[1] + ' not found')
      if elem == 'title':
        myentry[elem] = ('{' + val + '}')
      if elem in entries[myentry['type']]:
       	if not elem in myentry:
          myentry[elem] = val

add_entry()
fin.close()

mylist = sorted(mylist, key=lambda k: k['key']) 

# print bibtex entries
fout = open('mypapers.bib','w')
#for a in mylist.values():
#mymap = {}
#for a in mylist:
# mymap[a['key']] = a

proceedings = {}
#for a in mymap.values():
for a in mylist:
  if a['type'] == 'proceedings':
    #proceedings[a['key']] = a
    proceedings[a['key']] = collections.OrderedDict(sorted(a.items()))
  else:
    a = collections.OrderedDict(sorted(a.items()))
    fout.write('@' + a['type'] +'{' + a['key'] + ',\n')
    a.pop('key', None)
    a.pop('type', None)
    fout.write(',\n'.join('  {} = {{{}}}'.format(b, c) for b, c in a.items()))
    fout.write('\n}\n\n')

proceedings = collections.OrderedDict(sorted(proceedings.items()))
for a in proceedings.values():
  a = collections.OrderedDict(sorted(a.items()))
  fout.write('@' + a['type'] +'{' + a['key'] + ',\n')
  a.pop('key', None)
  a.pop('type', None)
  fout.write(',\n'.join('  {} = {{{}}}'.format(b, c) for b, c in a.items()))
  fout.write('\n}\n\n')
fout.close()


# print co-author list
#fout = open('mycoauthors.txt','w')
#fout.write('\n'.join('\item {} ({})'.format(a[0], a[1]) for a in myauthorlist.most_common()))
#fout.close()


#                   http://dx.doi.org/10.1007/978-3-642-31912-9_3
#http://link.springer.com/content/pdf/10.1007/978-3-642-31912-9_3.pdf


#url='http://link.springer.com/content/pdf/10.1007/978-3-642-31912-9_3.pdf'
#file_name='papers/test.pdf'

#try:
#    urlretrieve(url,file_name)
#except URLError as e:
#    print(e.reason)



