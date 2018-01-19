import re

from django.db import models


from elements import * 

class Textaufgabe(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField()
    bereich = models.CharField(max_length=10)
    inhalt = models.CharField(max_length=10)
    schwierigkeit = models.IntegerField()
    punkte = models.IntegerField()

    muster = r"#\[[^(\]#)]*\]#"


    def __str__(self):              # __unicode__ on Python 2
        return self.text



    def importiere(self,datei,name=""):

        aufgabe = open(datei).readlines()

        self.name=name
        
        self.text=""
        for i,zeile in enumerate(aufgabe):
            if i < len(aufgabe)-1:
                self.text += aufgabe[i]
            else:
                break

        info = aufgabe[len(aufgabe)-1].replace(' ','').split('#')

        self.bereich=info[0] 
        self.inhalt=info[1] 
        self.schwierigkeit=info[2] 
        self.punkte=int(info[3].replace("\n",""))
        try:
            self.save()
            print ("erfolgreich")
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
        
        var = self.variablen()

        aufgabentext=self.text
        for i,v in enumerate(var):
            print (v)
            ### Variablen ohne mathematische Bedeutung
            if v == "Person" or v == "Ort":
                aufgabentext=aufgabentext.replace(varoriginal[i], str(werte[i]))
            ### Variablen die f\"ur die Berechnung notwendig sind.
            else:
                aufgabentext=aufgabentext.replace(varoriginal[i], "$" + einheitLatex(str(werte[i])) + "$")


        return aufgabentext

    ##### Loesungen
    def loesung(self,werte):

        zahl=[]
        einheit=[]
        
        for w in werte:
            try:
                zahl.append(float(w.split(" ")[0]))
            except:
                zahl.append(w)
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


        ### Prozentrechnung
        if self.inhalt == "Prozentwert":
            var=self.variablen()

            for i,v in enumerate(var):
                if v == "G":
                    gw=zahl[i]
                if v == "p":
                    p=zahl[i]
                    

            ergebnis=latex(gw*p/100.0) 

            lsg="$" + ergebnis + "$"

            return lsg


        if self.inhalt == "Prozentsatz":
            var=self.variablen()

            for i,v in enumerate(var):
                if v == "W+":
                    wplus=zahl[i]
                if v == "p":
                    p=zahl[i]
                if v == "G":
                    gw=zahl[i]
                    

            ergebnis=latex((wplus-gw)/gw) 

            lsg="$" + ergebnis + "$"

            return lsg




        if self.inhalt == "Grundwert":
            var=self.variablen()

            for i,v in enumerate(var):
                if v == "W+":
                    wplus=zahl[i]
                if v == "p":
                    p=zahl[i]
                if v == "G":
                    gw=zahl[i]
                if v == "W":
                    pw=zahl[i]
                    

            ergebnis1=latex(pw/p*100)
            ergebnis2=latex(pw/p*100+pw)

            lsg="$" + ergebnis1 + "," + ergebnis2 + "$"

            return lsg





        else:
            return 0







