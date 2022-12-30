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

CrO = pd.read_table(r'CrO.tsv',header=3)
Cr2O3 = pd.read_table(r'Cr2O3.tsv',header=3)
Ti2O3 = pd.read_table(r'Ti2O3.tsv',header=3)
TiO2 = pd.read_table(r'TiO2.tsv',header=3)

fo2s = {'whoi4':'IW-0.29'
        ,'whoi2':'IW-0.83'
        ,'whoi5':'IW-2.27'
        ,'whoi3':'IW-3.30'
        }

    
#%% read in Cr glass

Cr_gl_whoi4 = readIntoList([r'C:\Users\r11403eb\OneDrive - The University of Manchester\Diamond\ascii\Cr\Glass\187771_WHOI4-gl-Cr_1.dat'
                              ,r'C:\Users\r11403eb\OneDrive - The University of Manchester\Diamond\ascii\Cr\Glass\187772_WHOI4-gl-Cr_1.dat'
                              ,r'C:\Users\r11403eb\OneDrive - The University of Manchester\Diamond\ascii\Cr\Glass\187776_WHOI4-gl-Cr_1.dat'
                              ])

Cr_gl_whoi2 = readIntoList(["C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Glass/187803_WHOI2-glass-Cr_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Glass/187800_WHOI2-glass-Cr_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Glass/187801_WHOI2-glass-Cr_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Glass/187802_WHOI2-glass-Cr_1.dat"
                            ])

Cr_gl_whoi5 = readIntoList(["C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Glass/187811_WHOI5-glass-Cr_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Glass/187808_WHOI5-glass-Cr_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Glass/187809_WHOI5-glass-Cr_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Glass/187810_WHOI5-glass-Cr_1.dat"
                            ])

Cr_gl_whoi3 = readIntoList(["C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Glass/187804_WHOI3-glass-Cr_1.dat"
                          ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Glass/187805_WHOI3-glass-Cr_1.dat"
                          ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Glass/187806_WHOI3-glass-Cr_1.dat"
                          ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Glass/187807_WHOI3-glass-Cr_1.dat"
                          ])
#%% read in Cr plag

Cr_plag_whoi4 = readIntoList(["C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Plag/187775_WHOI4-plag-Cr_1.dat"
                           ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Plag/187770_WHOI4-plag-Cr_1.dat"
                           ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Plag/187774_WHOI4-plag-Cr_1.dat"
                           ])

Cr_plag_whoi2 = readIntoList(["C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Plag/187799_WHOI2-plag-Cr_1.dat"
                              ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Plag/187796_WHOI2-plag-Cr_1.dat"
                              ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Plag/187797_WHOI2-plag-Cr_1.dat"
                              ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Plag/187798_WHOI2-plag-Cr_1.dat"
                              ])


Cr_plag_whoi5 = readIntoList(["C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Plag/187781_WHOI5-plag-Cr_1.dat"
                              ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Plag/187778_WHOI5-plag-Cr_1.dat"
                              ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Plag/187779_WHOI5-plag-Cr_1.dat"
                              ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Plag/187780_WHOI5-plag-Cr_1.dat"
                              ])

Cr_plag_whoi3 = readIntoList(["C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Plag/187788_WHOI3-plag-Cr_1.dat"
                                ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Plag/187786_WHOI3-plag-Cr_1.dat"
                                ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Cr/Plag/187787_WHOI3-plag-Cr_1.dat"
                                ])
#%% read in Ti gl

Ti_gl_whoi4 = readIntoList(["C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187754_WHOI4-map1_1.dat"
                              ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187755_WHOI4-map1_1.dat"
                              ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187756_WHOI4-map1_1.dat"
                              ])

Ti_gl_whoi2 = readIntoList(["C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187815_WHOI2-Ti-glass_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187812_WHOI2-Ti-glass_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187813_WHOI2-Ti-glass_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187814_WHOI2-Ti-glass_1.dat"
                            ])

Ti_gl_whoi5 = readIntoList(["C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187820_WHOI5-Ti-glass_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187821_WHOI5-Ti-glass_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187822_WHOI5-Ti-glass_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187823_WHOI5-Ti-glass_1.dat"
                            ])

Ti_gl_whoi3 = readIntoList(["C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187816_WHOI3-Ti-glass_1.dat"
                          ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187817_WHOI3-Ti-glass_1.dat"
                          ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187818_WHOI3-Ti-glass_1.dat"
                          ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Glass/187819_WHOI3-Ti-glass_1.dat"
                          ])

#%% read in Ti plag

Ti_plag_whoi4 = readIntoList(["C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187757_WHOI4-Plag_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187758_WHOI4-plagprofile_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187759_WHOI4-plagprofile_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187760_WHOI4-plagprofile_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187761_WHOI4-plagprofile_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187762_WHOI4-plagprofile_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187763_WHOI4-plagprofile_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187764_WHOI4-plagprofile_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187765_WHOI4-plagprofile_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187766_WHOI4-plagprofile_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187767_WHOI4-plagprofile_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187768_WHOI4-plagprofile_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187769_WHOI4-plagprofile_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187773_WHOI4-Ti-Plag_1.dat"
                              ])

Ti_plag_whoi4_new = []

for i in Ti_plag_whoi4:
    if len(i) == 276:
        Ti_plag_whoi4_new.append(i)
        
Ti_plag_whoi2 = readIntoList(["C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187795_WHOI2-Ti-Plag_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187791_WHOI2-Ti-Plag_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187792_WHOI2-Ti-Plag_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187793_WHOI2-Ti-Plag_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187794_WHOI2-Ti-Plag_1.dat"
                            ])

Ti_plag_whoi5 = readIntoList(["C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187784_WHOI5-Ti-Plag_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187782_WHOI5-Ti-Plag_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187783_WHOI5-Ti-Plag_1.dat"
                            ])

Ti_plag_whoi5_new = []

for i in Ti_plag_whoi5:
    if len(i) == 276:
        Ti_plag_whoi5_new.append(i)

Ti_plag_whoi3 = readIntoList(["C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187790_WHOI3-Ti-Plag_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187785_WHOI3-Ti-Plag_1.dat"
                            ,"C:/Users/r11403eb/OneDrive - The University of Manchester/Diamond/ascii/Ti/Plag/187789_WHOI3-Ti-Plag_1.dat"
                          ])

#%% work out derivs 


fig_Cr_gl,Cr_gl=plt.subplots()
fig_Cr_pl,Cr_pl=plt.subplots()

fig_Ti_gl,Ti_gl=plt.subplots()
fig_Ti_pl,Ti_pl=plt.subplots()

def calAndPlotDiff(window=[5994,5999]
                   ,movingAv=5
                   ,data_set=Cr_gl_whoi5
                   ,label=fo2s['whoi5']
                   ,axes=Cr_gl
                   ):
       
    df = pd.DataFrame()
    intensity=avFromList(data_set,'FF/I0_norm')
    df[intensity.name] = intensity
    df['Energy'] = data_set[0]['# Energy']
    df['diff'] = df['FF/I0_norm'].diff()
    df['diff_ma_5'] = df['diff'].rolling(window=movingAv).mean()
    
    axes.plot(df[(df['Energy'] >= window[0]-5) & (df['Energy'] <= window[1]+5)]['Energy']
              ,df[(df['Energy'] >= window[0]-5) & (df['Energy'] <= window[1]+5)]['diff_ma_5'],
              label=label)
    axes.set_xlabel('Energy (eV)')
    axes.set_ylabel('Derivative')
    axes.legend()

    return df

#Cr
Cr_gl_whoi4_df = calAndPlotDiff(data_set=Cr_gl_whoi4,label=fo2s['whoi4'],axes=Cr_gl)
calAndPlotDiff(data_set=Cr_gl_whoi2,label=fo2s['whoi2'],axes=Cr_gl)
calAndPlotDiff(data_set=Cr_gl_whoi5,label=fo2s['whoi5'],axes=Cr_gl)
Cr_gl_whoi3_df = calAndPlotDiff(data_set=Cr_gl_whoi3,label=fo2s['whoi3'],axes=Cr_gl)

calAndPlotDiff(data_set=Cr_plag_whoi4,label=fo2s['whoi4'],axes=Cr_pl)
calAndPlotDiff(data_set=Cr_plag_whoi2,label=fo2s['whoi2'],axes=Cr_pl)
calAndPlotDiff(data_set=Cr_plag_whoi5,label=fo2s['whoi5'],axes=Cr_pl)
calAndPlotDiff(data_set=Cr_plag_whoi3,label=fo2s['whoi3'],axes=Cr_pl)

#Ti
#window = [4965,5010]
window = [4967,4974]

calAndPlotDiff(data_set=Ti_gl_whoi4,label=fo2s['whoi4'],axes=Ti_gl,window=window)
calAndPlotDiff(data_set=Ti_gl_whoi2,label=fo2s['whoi2'],axes=Ti_gl,window=window)
calAndPlotDiff(data_set=Ti_gl_whoi5,label=fo2s['whoi5'],axes=Ti_gl,window=window)
calAndPlotDiff(data_set=Ti_gl_whoi3,label=fo2s['whoi3'],axes=Ti_gl,window=window)

calAndPlotDiff(data_set=Ti_plag_whoi4_new,label=fo2s['whoi4'],axes=Ti_pl,window=window)
calAndPlotDiff(data_set=Ti_plag_whoi2,label=fo2s['whoi2'],axes=Ti_pl,window=window)
calAndPlotDiff(data_set=Ti_plag_whoi5_new,label=fo2s['whoi5'],axes=Ti_pl,window=window)
calAndPlotDiff(data_set=Ti_plag_whoi3,label=fo2s['whoi3'],axes=Ti_pl,window=window)



#%% Area under plot 

x1 = 5994
x2 = 5999

baseline_area = (x2-x1)*max(Cr_gl_whoi3_df[(Cr_gl_whoi3_df['Energy'] >= x1) & (Cr_gl_whoi3_df['Energy'] <= x2)]['diff'])

np.trapz(Cr_gl_whoi3_df[(Cr_gl_whoi3_df['Energy'] >= x1) & (Cr_gl_whoi3_df['Energy'] <= x2)]['diff_ma_5'],x=Cr_gl_whoi3_df[(Cr_gl_whoi3_df['Energy'] >= x1) & (Cr_gl_whoi3_df['Energy'] <= x2)]['Energy'])/(baseline_area)

np.trapz(Cr_gl_whoi4_df[(Cr_gl_whoi4_df['Energy'] >= x1) & (Cr_gl_whoi4_df['Energy'] <= x2)]['diff_ma_5'],x=Cr_gl_whoi4_df[(Cr_gl_whoi4_df['Energy'] >= x1) & (Cr_gl_whoi4_df['Energy'] <= x2)]['Energy'])/(baseline_area)


#%% general plots
fig,ax = plt.subplots(2,2,figsize=(12,8))
#fig.tight_layout()

for i in [Cr_gl_whoi5,Cr_gl_whoi4,Cr_gl_whoi3,Cr_gl_whoi2]:
    ax[0,0].plot(i[0]['# Energy']
                  ,avFromList(i,'FF/I0_norm')
                  )
ax[0,0].set_title('Cr - Gl')
#ax[0,0].set_yscale('log')
ax[0,0].grid()

for i in [Cr_plag_whoi5,Cr_plag_whoi4,Cr_plag_whoi3,Cr_plag_whoi2]:
    ax[0,1].plot(i[0]['# Energy']
                  ,avFromList(i,'FF/I0_norm')
                  )
#ax[0,1].set_yscale('log')
ax[0,1].set_title('Cr - Plag')
ax[0,1].grid()


for i,j in zip([Ti_gl_whoi5,Ti_gl_whoi4,Ti_gl_whoi3,Ti_gl_whoi2],[fo2s['whoi5'],fo2s['whoi4'],fo2s['whoi3'],fo2s['whoi2']]):
    ax[1,0].plot(i[0]['# Energy']
                  ,avFromList(i,'FF/I0_norm')
                  ,label=j
                  )
ax[1,0].set_title('Ti - Gl')
ax[1,0].legend()
ax[1,0].grid()

for i in [Ti_plag_whoi5_new,Ti_plag_whoi4_new,Ti_plag_whoi3,Ti_plag_whoi2]:
    ax[1,1].plot(i[0]['# Energy']
                  ,avFromList(i,'FF/I0_norm')
                  )
ax[1,1].set_title('Ti - Plag')
ax[1,1].grid()


ax[0,0].set_xlim(5990,6010)
ax[0,1].set_xlim(5990,6010)

ax[1,0].set_xlim(4965,4990)
ax[1,1].set_xlim(4965,4990)

ax[1,0].set_xlabel('Energy eV')
ax[1,1].set_xlabel('Energy eV')

ax[0,0].set_ylabel('x\u03BC(E)')
ax[1,0].set_ylabel('x\u03BC(E)')
