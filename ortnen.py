#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 21:32:05 2019

@author: philipp
"""

import csv
import os
 
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

def rename_file(fname):
    """ 
    renames the file and a existing appendix
    """
    x,y=[],[]
    with open(fname,) as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            x.append(row[0])
            y.append(row[1])
    date=y[0].split(".")
    if len(y[2])<20:
        title=y[2]
    else:
        title=y[2][0:20]
    title=title.replace(" ","_")
    
    new_name="{}{}{}{}.csv".format(date[2],date[1],date[0],title)
    os.rename(fname,new_name)
    return new_name
    

with open('Beschluss02.csv',) as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        x.append(row[0])
        y.append(row[1])

c=y[11].split(",")
rename_file("Beschluss02.csv")
a=build_latex(y)
print(a)