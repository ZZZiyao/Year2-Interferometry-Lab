# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 06:44:42 2023

@author: xziya
"""
import numpy as np
import matplotlib.pyplot as plt
data=np.loadtxt('D:\\Y2 Lab\\Interferometry\\xyz.txt',unpack=True)
wavelength=data[0]
xx=data[1]/max(data[3])
yy=data[2]/max(data[3])
zz=data[3]/max(data[3])
data2=np.loadtxt('D:\\Y2 Lab\\Interferometry\\interpolated_data.txt',unpack=True)
lambda1=data2[0]
intensity=data2[1]  
yvals= intensity / max(intensity)
plt.plot(lambda1,yvals,label="E(λ)",color='orange')
plt.grid()
plt.xlabel('wavelength (nm)')
plt.ylabel('intensity(a.u.)')
#plt.title('White LED spectrum after flattening')

xxx=[]
yyy=[]
zzz=[]
for i in range(len(xx)):
    kk=yy[i]*yvals[i]
    yyy.append(kk)
for i in range(len(xx)):
    kk=xx[i]*yvals[i]
    xxx.append(kk)
for i in range(len(xx)):
    kk=zz[i]*yvals[i]
    zzz.append(kk)
plt.plot(lambda1,xxx/max(zzz),color='red',label='X(λ)')
plt.plot(lambda1,yyy/max(zzz),color='green',label='Y(λ)')
plt.plot(lambda1,zzz/max(zzz),color='dodgerblue',label='Z(λ)')
plt.legend()

from scipy.integrate import trapz,simps
integral_trapz = trapz(xxx/max(zzz),lambda1)
print("Integral using Trapezoidal Rule:", integral_trapz)
from scipy.integrate import trapz
integral_trapz2 = trapz(yyy/max(zzz),lambda1)
print("Integral using Trapezoidal Rule:", integral_trapz2)
from scipy.integrate import trapz
integral_trapz3 = trapz(zzz/max(zzz),lambda1)
print("Integral using Trapezoidal Rule:", integral_trapz3)
#%%
# 91.21,82.71,81.08
# 57.87,52.47,51.44
# 25.61±0.02, 21.40±0.01, 18.07±0.02
# 21.48±0.03, 22.06±0.04, and 20.22±0.02
X=51.92/56.26
Y=53.55/56.26
Z=56.26/56.26
# X=57.87/57.87
# Y=52.47/57.87
# Z=51.44/57.87
X=21.48/22.06
Y=1
Z=20.22/22.06
print(X,Y,Z)
R=2.37*X-0.9*Y-0.4785314*Z
G=-0.569266*X+1.425*Y+0.088556*Z
B=0.0053*X-0.0146949*Y+1.0093968*Z
print(R,G,B)
RR=R/B*255
GG=G/B*255
BB=B/B*255
print(RR,GG,BB)

n=(X-0.332*(X+Y+Z))/(0.1858*(X+Y+Z))
CCT=449*n**3+3525*n**2+6823.3*n+5520.33
print(CCT)
#6533.10
#5702.29

