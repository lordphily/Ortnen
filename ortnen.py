#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 21:32:05 2019

@author: philipp
"""

import csv
import os

def load_file(fname):
    x,y=[],[]
    with open(fname,) as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            x.append(row[0])
            y.append(row[1])
    return x,y

def replace_line(fname,line,new_line):
    lines = open(fname).read().splitlines()
    lines[line] = new_line
    open('output_file.csv','w').write('\n'.join(lines))
    os.remove(fname)
    os.rename("output_file.csv",fname)
    

def build_latex_standalone(x):
    """
    Mache aus x ein latex bereich des dokuments
    
    """
    eingabe=[]
    eingabe.append("\\title{%s}" %(x[2]))
    eingabe.append("\\author{%s}" %(x[1]))
    eingabe.append("\\date{%s}" %(x[0]))
    eingabe.append("\maketitle") 
    eingabe.append("\section{Infos}")
    eingabe.append("\\begin{tabularx}{\linewidth}{@{}lX}")
    eingabe.append(r"\textbf{Anatrag/Beschluss wurde} & %s\\" %(x[9]))
    x[11]=x[11].replace(" ","")
    kw=x[11].split(",")
    for i in range(0,len(kw)):
        if i==0:
            eingabe.append(r"\textbf{Keyword:} & %s\\" %(kw[i]))
        else:
            eingabe.append(r" & %s\\" %(kw[i]))
    eingabe.append("\end{tabularx}")
    eingabe.append("\\begin{tabularx}{\linewidth}{@{}XXX}")
    eingabe.append(r"\textbf{Abstimmungsergebniss:}&&\\")
    eingabe.append(r"Zustimmung & Ablehnung & Enthaltungen \\")
    eingabe.append(r"{} & {} & {} \\".format(x[6],x[7],x[8]))
    eingabe.append("\end{tabularx}")
    eingabe.append("\section{Antrags/Beschlusstext}")
    eingabe.append(x[3])
    eingabe.append("\section{Begründung}")
    eingabe.append(x[4])
    if x[23]=="Ja" and x[24]!="":
        delta=7
        anzahl=int((len(x)-23)/delta)
        if anzahl==1:
            eingabe.append("\section{Änderungsantrag}")
            eingabe.append("\subsection*{Vorschlag}")
            eingabe.append(x[24])
            eingabe.append("\subsection*{Begründung}")
            eingabe.append(x[25]+"\\vspace{1.5ex} \\\\")
            eingabe.append("\\begin{tabularx}{\linewidth}{@{}XXX}")
            eingabe.append(r"\textbf{Abstimmungsergebniss:}&&\\")
            eingabe.append(r"Zustimmung & Ablehnung & Enthaltungen \\")
            eingabe.append(r"{} & {} & {} \\".format(x[26],x[27],x[28]))
            eingabe.append(r"\multicolumn{@{}2}{l}{\textbf{Änderungsantrag wurde:}} & %s \\" %(x[29]))
            eingabe.append("\end{tabularx}")
        else:
            eingabe.append("\section{Änderungsanträge}")
            for i in range(0,anzahl):
                eingabe.append("\subsection{Änderungsvorschlag %s}" %(i+1))
                eingabe.append("\subsubsection*{Vorschlag}")
                eingabe.append(x[24+(delta*i)])
                eingabe.append("\subsubsection*{Begründung}")
                eingabe.append(x[25+(delta*i)]+"\\vspace{1.5ex} \\\\")
                eingabe.append("\\begin{tabularx}{\linewidth}{@{}XXX}")
                eingabe.append(r"\textbf{Abstimmungsergebniss:}&&\\")
                eingabe.append(r"Zustimmung & Ablehnung & Enthaltungen \\")
                eingabe.append(r"{} & {} & {} \\".format(x[26+(delta*i)],x[27+(delta*i)],x[28+(delta*i)]))
                eingabe.append(r"\multicolumn{@{}2}{l}{\textbf{Änderungsantrag wurde:}} & %s \\" %(x[29+(delta*i)]))
                eingabe.append("\end{tabularx}")
    if x[10]!="":
        #\includepdf[pages=-]{Anhang/Geschaeftsordnung_Jugendausschuss.pdf}
        eingabe.append("\\appendix")
        eingabe.append("\section*{Anhang}")
        anhang=x[10].split(",")
        bennenung=x[11].split(",")
        eingabe[14]=eingabe[14]+"\\vspace{1.5ex} \n Dieser Antrag enthält %s Anhänge: " %(len(anhang))
        for i in range(0,len(anhang)):
            eingabe.append("\subsection*{%s} \label{An:%s}" % (bennenung[i],str(i+1)))
            eingabe.append("%%\includepdf[pages=-]{%s}" %(anhang[i]))
            if i!=len(anhang)-1:
                eingabe[14]=eingabe[14]+"\\nameref{An:%s}, " % (str(i+1))
            else:
                eingabe[14]=eingabe[14]+"\\nameref{An:%s} " % (str(i+1))
                

    
    ausgabe=""
    for i in range(0,len(eingabe)):
        ausgabe=ausgabe+eingabe[i]+"\n"
    
    return ausgabe

def write_latex_standalone(fname):
    a=build_latex_standalone(load_file(fname)[1])
    pre=open("preamble.txt").read()
    doc=pre+a+"\n\\end{document}"
    path=os.getcwd()
    os.chdir("Ausgabe")
    fname_write=fname.split(".")[0]
    fname_write=fname_write+".tex"
    open(fname_write,"w").write(doc)
    os.chdir(path)
 
def build_latex(file_list):
    """
    Mache aus x ein latex bereich des dokuments
    
    """
    eingabe=[]
    anhang_count=0
    anhaenge=[]
    for file in file_list:
        x=load_file(file)[1]
        eingabe.append("\section{%s}"  %(x[2]))
        eingabe.append("\subsection{Infos}")
        eingabe.append("\\begin{tabularx}{\linewidth}{@{}lX}")
        eingabe.append(r"\textbf{Datum} & %s\\" %(x[0]))
        eingabe.append(r"\textbf{Gremium} & %s\\" %(x[1]))
        eingabe.append(r"\textbf{Anatrag/Beschluss wurde} & %s\\" %(x[9]))
        x[11]=x[11].replace(" ","")
        kw=x[11].split(",")
        for i in range(0,len(kw)):
            if i==0:
                eingabe.append(r"\textbf{Keyword:} & %s\\" %(kw[i]))
            else:
                eingabe.append(r" & %s\\" %(kw[i]))
        eingabe.append("\end{tabularx}")
        eingabe.append("\\begin{tabularx}{\linewidth}{@{}XXX}")
        eingabe.append(r"\textbf{Abstimmungsergebniss:}&&\\")
        eingabe.append(r"Zustimmung & Ablehnung & Enthaltungen \\")
        eingabe.append(r"{} & {} & {} \\".format(x[6],x[7],x[8]))
        eingabe.append("\end{tabularx}")
        eingabe.append("\subsection{Antrags/Beschlusstext}")
        line_text=len(eingabe)
        eingabe.append(x[3])
        eingabe.append("\subsection{Begründung}")
        eingabe.append(x[4])
        if x[23]=="Ja" and x[24]!="":
            delta=7
            anzahl=int((len(x)-23)/delta)
            if anzahl==1:
                eingabe.append("\subsection{Änderungsantrag}")
                eingabe.append("\subsubsection*{Vorschlag}")
                eingabe.append(x[24])
                eingabe.append("\subsubsection*{Begründung}")
                eingabe.append(x[25]+"\\vspace{1.5ex} \\\\")
                eingabe.append("\\begin{tabularx}{\linewidth}{@{}XXX}")
                eingabe.append(r"\textbf{Abstimmungsergebniss:}&&\\")
                eingabe.append(r"Zustimmung & Ablehnung & Enthaltungen \\")
                eingabe.append(r"{} & {} & {} \\".format(x[26],x[27],x[28]))
                eingabe.append(r"\multicolumn{2}{@{}l}{\textbf{Änderungsantrag wurde:}} & %s \\" %(x[29]))
                eingabe.append("\\end{tabularx}")
            else:
                eingabe.append("\subsection{Änderungsanträge}")
                for i in range(0,anzahl):
                    eingabe.append("\subsubsection{Änderungsvorschlag %s}" %(i+1))
                    eingabe.append("\\paragraph*{Vorschlag}")
                    eingabe.append(x[24+(delta*i)])
                    eingabe.append("\\paragraph*{Begründung}")
                    eingabe.append(x[25+(delta*i)]+"\\vspace{1.5ex} \\\\")
                    eingabe.append("\\begin{tabularx}{\linewidth}{@{}XXX}")
                    eingabe.append(r"\textbf{Abstimmungsergebniss:}&&\\")
                    eingabe.append(r"Zustimmung & Ablehnung & Enthaltungen \\")
                    eingabe.append(r"{} & {} & {} \\".format(x[26+(delta*i)],x[27+(delta*i)],x[28+(delta*i)]))
                    eingabe.append(r"\multicolumn{2}{@{}l}{\textbf{Änderungsantrag wurde:}} & %s \\" %(x[29+(delta*i)]))
                    eingabe.append("\\end{tabularx}")
        if x[10]!="":
            anhang=x[10].split(",")
            bennenung=x[11].split(",")
            eingabe[line_text]=eingabe[line_text]+"\\vspace{1.5ex} \n Dieser Antrag enthält %s Anhänge: " %(len(anhang))
            for i in range(0,len(anhang)):
                anhang_count=anhang_count+1
                anhaenge.append("\subsection*{%s - %s} \label{An:%s}" % (x[2],bennenung[i],str(anhang_count)))
                anhaenge.append("%%\includepdf[pages=-]{%s}" %(anhang[i]))
                if i!=len(anhang)-1:
                    eingabe[line_text]=eingabe[line_text]+"\\nameref{An:%s}, " % (str(anhang_count))
                else:
                    eingabe[line_text]=eingabe[line_text]+"\\nameref{An:%s} " % (str(anhang_count))   
    
    eingabe.append("\\appendix") 
    eingabe.append("\section*{Anhang}")         
    ausgabe=""
    for i in range(0,len(eingabe)):
        ausgabe=ausgabe+eingabe[i]+"\n"
 
    for i in range(0,len(anhaenge)):
        ausgabe=ausgabe+anhaenge[i]+"\n"
        
    return ausgabe

def write_latex_all(filelist):
    a=build_latex(filelist)
    pre=open("preamble_all.txt").read()
    doc=pre+a+"\n\\end{document}"
    path=os.getcwd()
    os.chdir("Ausgabe")
    open("Alles.tex","w").write(doc)
    os.chdir(path)

    
def rename_appendix(appendix,fname):
    """
    Bennent alle Files die im appendix sind um
    """
    listnewname=[]
    string=""
    if appendix!="":
        appendix=appendix.split(",")
        fname=fname.split(".")[0]
        for i in range(0,len(appendix)):
            new_name=fname+"_Anhang"+str(i+1)+".pdf"
            os.rename(appendix[i],new_name)
            listnewname.append(new_name)
        for i in range(0,len(listnewname)):
            if i!=0:
                string=string+","+listnewname[i]
            else:
                string=listnewname[i]
    return string   

def rename_file(fname):
    """ 
    renames the file and a existing appendix
    """
    x,y = load_file(fname)
    date=y[0].split(".")
    if len(y[2])<20:
        title=y[2]
    else:
        title=y[2][0:20]
    title=title.replace(" ","_")
    
    new_name="{}{}{}{}.csv".format(date[2],date[1],date[0],title)
    new_appendix=rename_appendix(y[10],new_name)
    os.rename(fname,new_name)
    replace_line(new_name,10,'Anhang;"{}"'.format(new_appendix))
    return new_name
    
filelist=[]
for filename in os.listdir():
    if filename.endswith(".csv"):
        rename_file(filename)
        filelist.append(filename)

a=build_latex_standalone(load_file(filelist[1])[1])
write_latex_standalone(filelist[0])
a=build_latex(filelist)
write_latex_all(filelist)
print(a)