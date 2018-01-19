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
filer=open('geraden1.tex','r')
filew=open('geraden1_py.tex','w')
for zeile in filer:
    zeiletmp=zeile.replace('\\','\\\\')
    zeile_new=zeiletmp.replace('\n',' \\n\\ \n')
    filew.write(zeile_new)
filer.close()
filew.close()
