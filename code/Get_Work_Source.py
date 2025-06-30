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
work_sources=pd.read_csv(os.path.join(data_dir,'works_primary_locations.csv'),chunksize=100000)

Dict_Work_Source=dict()
for chunk in tqdm(work_sources):
    for _,line in chunk.iterrows():
        work_id=int(line['work_id'].strip('https://openalex.org/W'))
        source_id=int(line['source_id'].strip('https://openalex.org/S'))
        if work_id in SelectWork_Year_TitleAbstract_Language and work_id in SelectWork_JournalConference:
            Dict_Work_Source[work_id]=source_id

with open(os.path.join('..','results',f'Dict_Work_Source'),'wb') as f:
    pickle.dump(Dict_Work_Source,f)