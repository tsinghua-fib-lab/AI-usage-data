import os
import setproctitle
setproctitle.setproctitle('AI Impact@haoqianyue')

import pickle
import pandas as pd
from tqdm import tqdm

data_dir=os.path.join('..','openalex','csv-files')

SelectSource_JournalConference=list()
sources=pd.read_csv(os.path.join(data_dir,'sources.csv'))

for _,line in tqdm(sources.iterrows()):
    # if pd.isna(line['issn']):
    #     continue

    if line['type'] not in ['journal','conference']:
        continue
    
    id=int(line['id'].strip('https://openalex.org/S'))
    
    SelectSource_JournalConference.append(id)

print(len(SelectSource_JournalConference))
pickle.dump(SelectSource_JournalConference,open(os.path.join('..','results','List_SelectSource_JournalConference'),'wb'))


SelectSource_JournalConference=set(SelectSource_JournalConference)
SelectWork_JournalConference=list()
works=pd.read_csv(os.path.join(data_dir,'works_primary_locations.csv'),chunksize=100000,usecols=['work_id','source_id'])

for chunk in tqdm(works):
    for _,line in chunk.iterrows():
        work_id=int(line['work_id'].strip('https://openalex.org/W'))
        source_id=int(line['source_id'].strip('https://openalex.org/S'))
        if source_id not in SelectSource_JournalConference:
            continue

        SelectWork_JournalConference.append(work_id)

print(len(SelectWork_JournalConference))
pickle.dump(SelectWork_JournalConference,open(os.path.join('..','results','List_SelectWork_JournalConference'),'wb'))