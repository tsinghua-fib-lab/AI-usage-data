import os
import setproctitle
setproctitle.setproctitle('AI Impact@haoqianyue')

import json
import pickle
import pandas as pd
from tqdm import tqdm

data_dir=os.path.join('..','openalex','csv-files')
sources=pd.read_csv(os.path.join(data_dir,'sources.csv'),chunksize=100000)

Dict_Source_Name=dict()
for chunk in tqdm(sources):
    for _,line in chunk.iterrows():
        id=int(line['id'].strip('https://openalex.org/S'))
        name=line['display_name']

        Dict_Source_Name[id]=name

with open(os.path.join('..','results',f'Dict_Source_Name'),'wb') as f:
    pickle.dump(Dict_Source_Name,f)