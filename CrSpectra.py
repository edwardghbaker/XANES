# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mp_api import MPRester
import atomate as at
import emmet as em 


import math as m
import numpy as np
import pandas as pd
import scipy.optimize as sciop
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.pyplot import figure



with MPRester(api_key="mNtEjiBMr7bH12r06xAKhtoycB50tR79") as mpr:
    data = mpr.xas.get_data_by_id("mp-1043379")
#%% load in data
CrO = pd.read_table(r'CrO.tsv',header=3)
Cr2O3 = pd.read_table(r'Cr2O3.tsv',header=3)
Ti2O3 = pd.read_table(r'Ti2O3.tsv',header=3)
TiO2 = pd.read_table(r'TiO2.tsv',header=3)

# CrO_fit = np.polyfit(CrO.iloc[:,0],CrO.iloc[:,1],1)
# Cr2O3_fit = np.polyfit(Cr2O3.iloc[:,0],Cr2O3.iloc[:,1],1)

#%% Generate figs
fig,[axCr,axTi] = plt.subplots(1,2,figsize=(8,4),sharey=True)
fig.tight_layout()

#fig_cr,axCr = plt.subplots(figsize=(6,4))
#fig_ti,axTi = plt.subplots(figsize=(6,4))

#%% Plot Chromium data

axCr.plot(CrO.iloc[:,0],CrO.iloc[:,1],label='$CrO$')
axCr.plot(Cr2O3.iloc[:,0],Cr2O3.iloc[:,1],label='$Cr_2O_3$')
axCr.set_xlim(5990,6010
              )
axCr.set_xlabel('eV')
axCr.set_ylabel('Intensity')
axCr.legend()
#fig_cr.savefig('Cr_spectrum.PNG',dpi=480)



#%% plot Ti data
for i in range(np.shape(Ti2O3)[1]):
    if(i%2 == 0):
        axTi.plot(Ti2O3.iloc[:,i],Ti2O3.iloc[:,i+1],lw=0.1,c='C0')
    else: next

for i in range(np.shape(TiO2)[1]):
    if(i%2 == 0):
        axTi.plot(TiO2.iloc[:,i],TiO2.iloc[:,i+1],lw=0.1,c='C1')
    else: next

evens_TiO2 = np.arange(0,np.shape(TiO2)[1],2)
odds_TiO2 = np.arange(1,np.shape(TiO2)[1],2)
av_eV_TiO2 = np.average(TiO2.iloc[:,evens_TiO2],axis=1)
av_mu_TiO2 = np.average(TiO2.iloc[:,odds_TiO2],axis=1)

evens_Ti2O3 = np.arange(0,np.shape(Ti2O3)[1],2)
odds_Ti2O3 = np.arange(1,np.shape(Ti2O3)[1],2)
av_eV_Ti2O3 = np.average(Ti2O3.iloc[:,evens_Ti2O3],axis=1)
av_mu_Ti2O3 = np.average(Ti2O3.iloc[:,odds_Ti2O3],axis=1)

axTi.plot(av_eV_Ti2O3,av_mu_Ti2O3,label='$Ti_2O_3$',lw=1,c='C0')
axTi.plot(av_eV_TiO2,av_mu_TiO2,label='$TiO_2$',lw=1,c='C1')
axTi.set_xlabel('eV')
#axTi.set_ylabel('Intensity')
axTi.legend()
#fig_ti.savefig('Ti_spectrum.PNG',dpi=480)

fig.savefig('CrTi_spec.PNG',dpi=480)