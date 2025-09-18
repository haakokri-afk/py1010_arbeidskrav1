# -*- coding: utf-8 -*-
"""
Arbeidskrav 1

Created on Sun Sep 14 20:23:10 2025

@author: haako
"""

D = 10000 # Antall km per år
FE = 5000 # Forsikring elbil per år
FB = 7500 # Forsikring bensinbil per år
T = 8.38*365 # Trafikkforsikringsavgift per år
DE = D*(0.2*2) # Drivstofforbruk elbil (forbruk 0,2kWm/km og pris kr 2,0/kWm)
DB = D*1 # Drivstofforbruk bensinbil (kr 1 per km)
BE = D*0.1 # Bomavgift elbil (kr 0,1 per km)
BB = D*0.3 # Bomavgift bensinbil (kr 0,3 per km)
E = FE + T + DE + BE # Årlig kostnad elbil
B = FB + T + DB + BB # Årlig kostnad bensinbil
print("Årlig kostnad elbil = kr", E)
print("Årlig kostnad bensinbil = kr", B)
print("Differanse = kr", B-E)