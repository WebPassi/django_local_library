#! /usr/bin/env python

### While 1 ...
"""
file=open('test.txt','r')
try:
    while 1:
        zeile=file.readline()
        liste=zeile.split(', ')
        print liste[1]
except:
    print 'Ende'
    file.close()
"""

### Leerzeichen loeschen, Kommas anfuegen
filer=open('schueler.csv','r')
filew=open('schueler_uni.csv','w')
for zeile in filer:
    zeile_new=zeile.replace('\n',',,\n')
    filew.write(zeile_new.replace(' ',''))
filer.close()
filew.close()
