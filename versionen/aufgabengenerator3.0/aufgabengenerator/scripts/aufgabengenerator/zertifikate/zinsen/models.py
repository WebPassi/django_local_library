from django.db import models

# Create your models here.

class Aufgabe(models.Model):
    text = models.TextField()
    bereich = models.CharField(max_length=10)
    inhalt = models.CharField(max_length=10)
    schwierigkeit = models.IntegerField()
    punkte = models.IntegerField()


    def importiere(self):
        aufgabe = open('aufgaben_src/aufgabe.txt').readlines()
        aufg_text = aufgabe[0]
        meta = aufgabe[1].replace(' ','')
        print meta
        info = meta.split('#')
        aufgabe_db = Aufgabe(text=aufg_text, bereich=info[0], inhalt=info[1], schwierigkeit=info[2], punkte=info[3])
        try:
            aufgabe_db.save()
        except:
            print aufgabe_db.text
        
    def __str__(self):              # __unicode__ on Python 2
        return self.text
'''            
    def importiere(self):
        aufgabe = open('aufgaben_src/aufgabe.txt').readlines()
        aufg_text = aufgabe[0]
        print aufg_text
#            meta = zeile[1]
#        info = meta.split('#')
#        print aufg_text
        #aufgabe.close()
'''
