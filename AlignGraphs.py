# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 21:47:39 2022

@author: r11403eb
"""



import os as os 
import numpy as np
from tqdm import tqdm 
import pandas as pd
import matplotlib.pyplot as plt
pi = np.pi

#%% 

def norm(df,col):
    df[str(col+'_norm')] = df[col]/max(df[col])
    return df 

def readIntoList(array_of_files):
        
    listName = [pd.read_table(i,header=28) for i in array_of_files]
    for i in listName:
        i.columns = i.columns.str.strip()
    listName = [norm(i,'FF/I0') for i in listName]
    
    return listName

def avFromList(listofDF,col):
    x = np.zeros(len(listofDF[0]))
    for i in range(len(listofDF)):
        x+=listofDF[i][col]
    x=x/len(listofDF)
    return x
        
    
#%%

Cr_gl_oxi = readIntoList([r'C:\Users\r11403eb\OneDrive - The University of Manchester\Diamond\ascii\Cr\Glass\187771_WHOI4-gl-Cr_1.dat'
                              ,r'C:\Users\r11403eb\OneDrive - The University of Manchester\Diamond\ascii\Cr\Glass\187772_WHOI4-gl-Cr_1.dat'
                              ,r'C:\Users\r11403eb\OneDrive - The University of Manchester\Diamond\ascii\Cr\Glass\187776_WHOI4-gl-Cr_1.dat'
                              ])

Cr_gl_reduced = readIntoList(["C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Glass/187804_WHOI3-glass-Cr_1.dat"
                          ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Glass/187805_WHOI3-glass-Cr_1.dat"
                          ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Glass/187806_WHOI3-glass-Cr_1.dat"
                          ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Glass/187807_WHOI3-glass-Cr_1.dat"
                          ])

Ti_gl_oxi = readIntoList(["C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187754_WHOI4-map1_1.dat"
                              ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187755_WHOI4-map1_1.dat"
                              ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187756_WHOI4-map1_1.dat"
                              ])

# "C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187753_WHOI4-map1_1.dat"

Ti_gl_reduced = readIntoList(["C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187816_WHOI3-Ti-glass_1.dat"
                          ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187817_WHOI3-Ti-glass_1.dat"
                          ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187818_WHOI3-Ti-glass_1.dat"
                          ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187819_WHOI3-Ti-glass_1.dat"
                          ])



#%%
fig,ax = plt.subplots(2,2,figsize=(12,8))

ax[0,0].plot(Cr_gl_reduced[0]['# Energy']
              ,avFromList(Cr_gl_reduced,'FF/I0_norm')
              )
ax[0,0].set_title('Cr, IW-3.3')

ax[0,1].plot(Cr_gl_oxi[0]['# Energy']
              ,avFromList(Cr_gl_oxi,'FF/I0_norm')
              )
ax[0,1].set_title('Cr, IW-0.3')

ax[1,0].plot(Ti_gl_reduced[0]['# Energy']
              ,avFromList(Ti_gl_reduced,'FF/I0_norm')
              )
ax[1,0].set_title('Ti, IW-3.3')

ax[1,1].plot(Ti_gl_oxi[0]['# Energy']
              ,avFromList(Ti_gl_oxi,'FF/I0_norm')
              )
ax[1,1].set_title('Ti, IW-0.3')

ax[0,0].set_xlim(5900,6100)
ax[0,1].set_xlim(5900,6100)

ax[1,0].set_xlim(4900,5100)
ax[1,1].set_xlim(4900,5100)

ax[1,0].set_xlabel('Energy eV')
ax[1,1].set_xlabel('Energy eV')

ax[0,0].set_ylabel('x\u03BC(E)')
ax[1,0].set_ylabel('x\u03BC(E)')

# ax[1,0].text(0.5, 0.5, 'Ti, ', horizontalalignment='center',
#      verticalalignment='center', transform=ax[1,0].transAxes)




