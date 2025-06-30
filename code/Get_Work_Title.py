import os
import setproctitle
setproctitle.setproctitle('AI Impact@haoqianyue')

import json
import pickle
import pandas as pd
from tqdm import tqdm

with open(os.path.join('..','results','List_SelectWork_Year1980-2025_TitleAbstract_Language'),'rb') as f:
    SelectWork_Year_TitleAbstract_Language=set(pickle.load(f))
with open(os.path.join('..','results','List_SelectWork_JournalConference'),'rb') as f:
    SelectWork_JournalConference=set(pickle.load(f))

data_dir=os.path.join('..','openalex','csv-files')
works=pd.read_csv(os.path.join(data_dir,'works.csv'),chunksize=100000,usecols=['id','title'])

Dict_Work_Title=dict()
for chunk in tqdm(works):
    for _,line in chunk.iterrows():
        id=int(line['id'].strip('https://openalex.org/W'))
        if id in SelectWork_Year_TitleAbstract_Language and id in SelectWork_JournalConference:
            title=line['title']
            Dict_Work_Title[id]=title

with open(os.path.join('..','results',f'Dict_Work_Title'),'wb') as f:
    pickle.dump(Dict_Work_Title,f)