import re

from django.db import models


from elements import * 

class Textaufgabe(models.Model):
    text = models.TextField()
    bereich = models.CharField(max_length=10)
    inhalt = models.CharField(max_length=10)
    schwierigkeit = models.IntegerField()
    punkte = models.IntegerField()

    muster = r"#\[[^(\]#)]*\]#"


    def __str__(self):              # __unicode__ on Python 2
        return self.text



    def importiere(self,datei):

        aufgabe = open(datei).readlines()
        info = aufgabe[1].replace(' ','').split('#')

        self.text=aufgabe[0] 
        self.bereich=info[0] 
        self.inhalt=info[1] 
        self.schwierigkeit=info[2] 
        self.punkte=info[3]
        try:
            self.save()
        except:
            print (self.text)
        


    def variablen(self):
        varoriginal = re.findall(self.muster,self.text)
        var=[]

        for v in varoriginal:
            var.append(v.replace('#[','').replace(']#',''))

        return var              


    def erzeugeAufgabe(self,werte):
        varoriginal = re.findall(self.muster,self.text)
        

        aufgabentext=self.text
        for i,v in enumerate(varoriginal):
            aufgabentext=aufgabentext.replace(varoriginal[i], "$" + einheitLatex(str(werte[i])) + "$")

        return aufgabentext


    def loesung(self,werte):

        zahl=[]
        einheit=[]
        for w in werte:
            zahl.append(float(w.split(" ")[0]))
            try:
                einheit.append(w.split(" ")[1])
            except:
                einheit.append("")
            

        if self.inhalt == "Term":
            var=self.variablen()
            
            ergebnis=1.0
            for i,v in enumerate(var):
                if v == "Dividend":
                    dividend_zahl=zahl[i]
                    dividend_einheit=einheit[i]
                    ergebnis=ergebnis*zahl[i]*normiereEinheit(einheit[i])
                elif v == "Divisor":
                    divisor_zahl=zahl[i]
                    divisor_einheit=einheit[i]
                    ergebnis=ergebnis/(zahl[i]*normiereEinheit(einheit[i]))
                

            lsg="$\\frac{" + latex(dividend_zahl) + einheitLatex(dividend_einheit) + "}{" + latex(divisor_zahl) + einheitLatex(divisor_einheit) + "} = \\frac{" + latex(dividend_zahl) + latex(normiereEinheitZehnerpotenz(dividend_einheit)) + einheitLatex(einheitNorm(dividend_einheit)) + "}{" + latex(divisor_zahl) + latex(normiereEinheitZehnerpotenz(divisor_einheit)) + einheitLatex(einheitNorm(divisor_einheit)) + "}=" + latex(ergebnis) + einheitLatex(einheitenRechnerDiv(grundeinheit(dividend_einheit),grundeinheit(divisor_einheit))) + "$"
            return lsg


        if self.inhalt == "Wurzel":
            var=self.variablen()


            for i,v in enumerate(var):
                if v == "Wurzel":
                    ergebnis=latex(sqrt(zahl[i]*normiereEinheit(einheit[i])))
        
            lsg="$\\sqrt{" + latex(zahl[i]) + einheitLatex(einheit[i]) + "}=\\sqrt{" + latex(zahl[i]) + normiereEinheitZehnerpotenz(einheit[i]) + einheitLatex(grundeinheit(einheit[i])) + "}=" + ergebnis + einheitLatex(einheitNorm(einheit[i])) + "$"
            
            return lsg



        else:
            return 0







