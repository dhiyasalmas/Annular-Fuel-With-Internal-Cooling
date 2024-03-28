import numpy as np
import matplotlib.pyplot as plt
import math

'''
    UTS, Termodinamika Reaktor Nuklir
    Dhiya Salma Salsabila/24923304
'''

#Constant
qv = 100 #Volumetric heat rate (W/cc)
kf = 0.024 #Heat trans coef of fuel (W/cm.K)

#Fuel radial dimensions
r1 = 0.5 #Inner (cm)
r2 = 1 #Outer (cm)
rr1 = np.arange(0.5, 1.05, 0.05)

#Temperature
t1 = 350+273.15 #Fuel Surface temperature inner
t2 = t1 #Fuel Surface temperature outer

c1 = round((t1-t2)/(math.log(r1/r2))+(qv*(r1**2-r2**2))/(kf*4*(math.log(r1/r2))),2)
c2 = round(t1 - ((t1-t2)/(math.log(r1/r2))+(qv*(r1**2-r2**2)/(kf*4*(math.log(r1/r2)))))*math.log(r1)+(qv/kf)*(r1**2/4),2)
print(c1,c2)

tfuel = []
for i in range(len(rr1)):
    if i ==0:
        tr = round((-qv*rr1[i]**2)/(4*kf)+(c1*math.log(rr1[i]))+c2,2)
    else:
        tr = round((-qv*rr1[i]**2)/(4*kf)+(c1*math.log(rr1[i]))+c2,2)
    tfuel.append(tr)
    i += 1
print(tfuel)

plt.plot(rr1,tfuel)
plt.ylabel("Temperatur (K)")
plt.xlabel("Jari-Jari (cm)")
plt.title("Grafik Fuel Annular Pellet")
plt.show()