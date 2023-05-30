# -*- coding: utf-8 -*-
"""
Created on Tue May 31 15:43:30 2022

@author: Ed
"""
#%%
import numpy as np
import pandas as pd
import os as os
from matplotlib import cm
import matplotlib.pyplot as plt



#%% Info

'''

Key for Dataframe 'data'
f = failed scan 
? = unknown/test scan
x = crystal 
g = glass

To Do
1. read in experimental details

'''
#%% For processing 

def fo2_logic(string):
    WHOI1 = -0.7678
    WHOI2 = -0.8267
    WHOI3 = -3.301
    WHOI4 = -0.2919
    WHOI5 = -2.2747
    
    if string == 'WHOI1':
        fo2 = WHOI1
    elif string == 'WHOI2':
        fo2 = WHOI2
    elif string == 'WHOI3':
        fo2 = WHOI3
    elif string == 'WHOI4':
        fo2 = WHOI4
    else:
        fo2 = WHOI5
    return fo2

def norm(arr):
    return arr/max(arr)



#%% Read in data 

directory = 'C:/Users/User/OneDrive - The University of Manchester/Diamond/ascii'
fileNames = os.listdir(directory)

main = pd.DataFrame({'Phase' :['?','g','g','?','f','f','f','f','f','f','g','g','g','g','g','x','x','x','g','g','x','x','x','g','g','x','x','x','x','f','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
                     'Experiment' :['WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI4','WHOI5','WHOI5','WHOI5','WHOI5','WHOI5','WHOI5','WHOI5','WHOI5','WHOI3','WHOI3','WHOI3','WHOI3','WHOI3','WHOI3','WHOI2','WHOI2','WHOI2','WHOI2','WHOI2','WHOI2','WHOI2','WHOI2','WHOI2','WHOI2','WHOI2','WHOI2','WHOI2','WHOI3','WHOI3','WHOI3','WHOI3','WHOI4','WHOI4','WHOI4','WHOI4','WHOI2','WHOI2','WHOI2','WHOI2','WHOI3','WHOI3','WHOI3','WHOI3','WHOI4','WHOI4','WHOI4','WHOI4'],
                     'Element' : ['Ti','Ti','Ti','Ti','Ti','Ti','Ti','Ti','Ti','Ti','Ti','Ti','Ti','Ti','Ti','Ti','Ti','Cr','Cr','Cr','Ti','Cr','Cr','Cr','Cr','Cr','Cr','Cr','Cr','Ti','Ti','Ti','Ti','Cr','Cr','Cr','Ti','Ti','Ti','Ti','Ti','Ti','Ti','Cr','Cr','Cr','Cr','Cr','Cr','Cr','Cr','Cr','Cr','Cr','Cr','Cr','Cr','Cr','Cr','Ti','Ti','Ti','Ti','Ti','Ti','Ti','Ti','Ti','Ti','Ti','Ti']},
                    index = ['187753','187754','187755','187756','187757','187758','187759','187760','187761','187762','187763','187764','187765','187766','187767','187768','187769','187770','187771','187772','187773','187774','187775','187776','187777','187778','187779','187780','187781','187782','187783','187784','187785','187786','187787','187788','187789','187790','187791','187792','187793','187794','187795','187796','187797','187798','187799','187800'                    ,'187801','187802','187803','187804','187805','187806','187807','187808','187809','187810','187811','187812','187813','187814','187815','187816','187817','187818','187819','187820','187821','187822','187823'])

main['fo2'] = [fo2_logic(i) for i in main['Experiment']]
main['data'] = [pd.read_csv(str(directory+'/'+i),header=28,sep="\s+") for i in fileNames]

whoi = pd.read_excel(r'C:\Users\User\OneDrive - The University of Manchester\Experiments\CrTi in plagioclase\WHOI experiments.xlsx',sheet_name='Tabelle1',header=1,index_col = 0)

whoi1 = main[main.Experiment == 'WHOI1']
whoi2 = main[main.Experiment == 'WHOI2']
whoi3 = main[main.Experiment == 'WHOI3']
whoi4 = main[main.Experiment == 'WHOI4']
whoi5 = main[main.Experiment == 'WHOI5']

#%% Plot up the different spectra

'''

Now I will make a subplots figure for the glass/crystal and for the Cr and Ti, just to show the differences between all the different groups. 

'''

summary, [[Cr_plag,Cr_glass],[Ti_plag,Ti_glass]] = plt.subplots(2,2,figsize=(8,8),sharey=(True))
summary.tight_layout()
Ti_plag.set_xlabel('eV')
Ti_glass.set_xlabel('eV')

paired = cm.get_cmap('Paired')
xyz = [0,0,0,0]
for i in main.index:
    datum = main.loc[i]

    if datum.Phase == 'x' and datum.Element == 'Cr':
        if xyz[0] < 1:
            Cr_plag.plot(datum.data['#'],norm(datum.data['FF']/datum.data['I0']),
                         color=paired(np.abs(datum['fo2'])),
                         label=(str(datum['fo2'])))
            Cr_plag.legend()
        else:
            Cr_plag.plot(datum.data['#'],norm(datum.data['FF']/datum.data['I0']),
                         color=paired(np.abs(datum['fo2'])))
        xyz[0] =+ 1
        
        
    elif datum.Phase == 'g' and datum.Element == 'Cr':
        if xyz[1] < 1:
            Cr_glass.plot(datum.data['#'],norm(datum.data['FF']/datum.data['I0']),
                         color=paired(np.abs(datum['fo2'])),
                         label=(str(datum['fo2'])))
            Cr_glass.legend()
        else:
            Cr_glass.plot(datum.data['#'],norm(datum.data['FF']/datum.data['I0']),
                         color=paired(np.abs(datum['fo2'])))
        xyz[1] =+ 1
        
        
    elif datum.Phase == 'x' and datum.Element == 'Ti':
        if xyz[2] < 1:
            Ti_plag.plot(datum.data['#'],norm(datum.data['FF']/datum.data['I0']),
                         color=paired(np.abs(datum['fo2'])),
                         label=(str(datum['fo2'])))
            Ti_plag.legend()
        else:
            Ti_plag.plot(datum.data['#'],norm(datum.data['FF']/datum.data['I0']),
                         color=paired(np.abs(datum['fo2'])))
        xyz[2] =+ 1
        
        
    elif datum.Phase == 'g' and datum.Element == 'Ti':
        if xyz[3] < 1:
            Ti_glass.plot(datum.data['#'],norm(datum.data['FF']/datum.data['I0']),
                         color=paired(np.abs(datum['fo2'])),
                         label=(str(datum['fo2'])))
            Ti_glass.legend()
        else:
            Ti_glass.plot(datum.data['#'],norm(datum.data['FF']/datum.data['I0']),
                         color=paired(np.abs(datum['fo2'])))
        xyz[3] =+ 1
        
        
    else:
        next
        
#%% 

