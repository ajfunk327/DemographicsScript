import os
import glob
import pandas as pd
import csv
import numpy as np


all_filenames = [i for i in glob.glob('ParticipantData*.csv')]

combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

f = open('combined_csv.csv')

data = list(csv.reader(f))
data2 = np.array(data)
data3 =  []

for i in range (0, len(data)):
   if data2[i,2].startswith('-',0):
      continue
   elif data2[i,2].startswith('0',0): 
      continue
   elif data2[i,2].startswith('TRIAL',0):
      continue
   else:
      data3.append(data[i])


with open("AGGREGATE_DATA.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['PARTICIPANT', 'SCENE', 'TRIAL', 'BLOCK', 'HANDDOM', 'ARMLENGHT', 'PI', 'DISTANCE', 'CONDITION', 'RESPONSE', 'RESPONSE TIME'])
    writer.writerows(data3)

os.remove('combined_csv.csv')

print("AGGREGATED DATA FILE MADE")