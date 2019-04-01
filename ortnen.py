#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 21:32:05 2019

@author: philipp
"""

import csv
 
def build_latex(x,y):
    """
    Mache aus x und y ein Latex Dokument
    """
    eingabe=[]
    eingabe.append("\section{%s}" %(y[2]))
    eingabe.append("\ \bbegin{tabular}{ll}")
    eingabe.append(r"Abstimmendes Gremium: & %s\\" %(y[1]))
    eingabe.append(r"Datum: & %s\\" %(y[0]))
    eingabe.append(r"Anatrag/Beschluss wurde: & %s\\" %(y[9]))
    y[11]=y[11].replace(" ","")
    kw=y[11].split(",")
    for i in range(0,len(kw)):
        if i==0:
            eingabe.append(r"Keyword: & %s\\" %(kw[i]))
        else:
            eingabe.append(r" & %s\\" %(kw[i]))
    eingabe.append("\end{tabular}")
    eingabe.append("\ \bbegin{tabular}{ccc}")
    eingabe.append(r"\multicolumn{3}{c}{Abstimmungsergebniss}\\")
    eingabe.append(r"Zustimmung & Ablehnung & Enthaltungen \\")
    eingabe.append(r"{} & {} & {} \\".format(y[6],y[7],y[8]))
    eingabe.append("\end{tabular}")
    eingabe.append("\subsection*{Antragstext}")
    eingabe.append(y[3])
    eingabe.append("\subsection*{Begründung}")
    eingabe.append(y[4])

    
    ausgabe=""
    for i in range(0,len(eingabe)):
        ausgabe=ausgabe+eingabe[i]+"\n"
    
    return ausgabe
    
x,y=[],[]

with open('Beschluss01.csv',) as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        x.append(row[0])
        y.append(row[1])

c=y[11].split(",")
a=build_latex(x,y)
print(a)