# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 01:15:04 2023

@author: xziya
"""

###################################################################################################
### A little program that reads in the data and plots it
### You can use this as a basis for you analysis software 
###################################################################################################
def read_data3(fname):
    ######################################################################
    # A function that reads in the file. Modified from DJC 1/10/2018 by AC 4/03/20
    # Calling arguements:
    #     fname = name of txt file 
    #A better version of read_data2 that extract info out of a text file of any length i with result : [[0], [1], ...... [i]] where [i] is the array containing all the info of the ith column of the txt, all numbers are float, carefull when we have a single column: [ [0] ] array within array !
    
    #3rd - modif to store file names and not floats anymore - used to sort out the export procedure
    ######################################################################
    file = open(fname,"r")#, encoding='mac_roman')
    
    lines= file.readlines()
    signal=[[]]
    i=0
    j=0
    for k in lines[0]:
        #print (k)
        if k == ' ':
            signal.append([])
    #print(signal)
    for line in range(0,len(lines)):
        #print(line,'line')
        j=0
        i=0
        while j<=len(lines[line]) and i<=len(lines[line])-2:   #careful the 2 has been changed here, it was a 1 before !
            dd='' 
            #print(i,j)
            #print(signal)
            while lines[line][i]!=' ' and i<=len(lines[line])-2:
                dd=dd+lines[line][i]
                i=i+1
            
            #print(j)
            #print(dd)
            signal[j].append(float(dd))
            j=j+1
            i=i+1
            
            
    file.close()
    return signal



#file='Result_simu_26_02_f50_V0.26_fsamp9_Tg_a.txt_t0=0_l150_j50.txt'

#file='27_02_f80_g82_h_00_B3_C3D00_fsamp5_Tg_a.txt'

#sig=read_data3(file)
#print(sig)
import sys
import numpy as np
import matplotlib.pyplot as plt


# #Step 1 get the data and the x position
file='D:\Y2 Lab\Interferometry\white4.txt'#this is the data
results = read_data3(file)


y1 = np.array(results[0])
y2 = np.array(results[1])

x=np.array(results[5])

plt.figure("Detector 1")
plt.plot(x,y1,'o-')
plt.xlabel("Position $\mu$steps]")
plt.ylabel("Signal 1")
plt.show()


plt.figure("Detector 2")
plt.plot(x,y2,'o-')
plt.xlabel("Position $\mu$steps]")
plt.ylabel("Signal 2")
plt.savefig("figures/quick_plot_detector_2.png")


#%%
import plotly.graph_objects as go
import pandas as pd
from scipy.signal import find_peaks


time_series = y1


indices = find_peaks(time_series)[0]

i_indices=[]

peaks=[]
for i in range(len(indices)):
    numaa=indices[i]
    if y1[numaa]>3400000:
      peaks.append(y1[numaa])
      i_indices.append(x[numaa])

plt.scatter(i_indices[95:104],peaks[95:104],s=8,marker='x',color='r',linewidths=20)

steps=[]
for i in range(len(i_indices)-1):
    space=i_indices[i]-i_indices[i+1]
    steps.append(space)
print(steps)
print('average distance between peaks is',np.mean(steps))
print("standard deviation of distances is",np.std(steps))
plt.show()




    