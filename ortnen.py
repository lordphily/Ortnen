#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 21:32:05 2019

@author: philipp
"""

import csv
 
def build_latex(x):
    """
    Mache aus x ein latex bereich des dokuments
    
    """
    eingabe=[]
    eingabe.append("\section{%s}" %(x[2]))
    eingabe.append("\ \bbegin{tabularx}{\linewidth}{lX}")
    eingabe.append(r"\textbf{Abstimmendes Gremium:} & %s\\" %(x[1]))
    eingabe.append(r"\textbf{Datum:} & %s\\" %(x[0]))
    eingabe.append(r"\textbf{Anatrag/Beschluss wurde} & %s\\" %(x[9]))
    x[11]=x[11].replace(" ","")
    kw=x[11].split(",")
    for i in range(0,len(kw)):
        if i==0:
            eingabe.append(r"\textbf{Keyword:} & %s\\" %(kw[i]))
        else:
            eingabe.append(r" & %s\\" %(kw[i]))
    eingabe.append("\end{tabularx}")
    eingabe.append("\ \bbegin{tabularx}{\linewidth}{XXX}")
    eingabe.append(r"\multicolumn{3}{l}{\textbf{Abstimmungsergebniss:}}\\")
    eingabe.append(r"Zustimmung & Ablehnung & Enthaltungen \\")
    eingabe.append(r"{} & {} & {} \\".format(x[6],x[7],x[8]))
    eingabe.append("\end{tabularx}")
    eingabe.append("\subsection*{Antragstext}")
    eingabe.append(x[3])
    eingabe.append("\subsection*{Begründung}")
    eingabe.append(x[4])
    if x[10]!="":
        eingabe.append("\subsection{Anhang}")
        eingabe.append(x[10])
    
    ausgabe=""
    for i in range(0,len(eingabe)):
        ausgabe=ausgabe+eingabe[i]+"\n"
    
    return ausgabe
    
x,y=[],[]

with open('Beschluss02.csv',) as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        x.append(row[0])
        y.append(row[1])

c=y[11].split(",")
a=build_latex(y)
print(a)