# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

data1 = open("temperatur_trykk_met_samme_rune_time_datasett.csv", "r", encoding="UTF8")

linjer1 = data1.readlines()[1:]

for linje in data1:
    print(linje)

"""navn = []
stasjon = []
tid = []
lufttemperatur = []
lufttrykk = []

for linje in data1:
    print(linje)
   navn.append(linje[0])
   stasjon.append(linje[1])
   tid.append(linje[2])
   lufttemperatur.append(linje[3])
   lufttrykk.append(linje[4])"""
   
data1.close()
    

    






