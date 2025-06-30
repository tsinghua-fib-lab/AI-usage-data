import os
import setproctitle
setproctitle.setproctitle('AI Impact@haoqianyue')

import pickle
import numpy as np
import pandas as pd
from tqdm import tqdm


with open(os.path.join('..','result','Dict_ClassifyWork_UnionValue'),'rb') as f:
    paper_AI_classify=pickle.load(f)
with open(os.path.join('..','result','Dict_Work_Date'),'rb') as f:
    paper_date=pickle.load(f)
with open(os.path.join('..','result','Dict_Work_Title'),'rb') as f:
    paper_title=pickle.load(f)
with open(os.path.join('..','result','Dict_Work_Source'),'rb') as f:
    paper_source=pickle.load(f)

with open(os.path.join('..','result','Dict_Source_Name'),'rb') as f:
    source_name=pickle.load(f)


IDs=list()
titles=list()
dates=list()
venues=list()
classifies=list()

venue_paper_count=dict()

for PaperID,classify in tqdm(paper_AI_classify.items()):
    try:        
        title=paper_title[PaperID]
        date=paper_date[PaperID]
        venue=paper_source[PaperID]
    except:
        continue

    IDs.append(PaperID)
    titles.append(title)
    dates.append(date)
    venues.append(venue)
    classifies.append(classify)

    if venue not in venue_paper_count:
        venue_paper_count[venue]=list()
    venue_paper_count[venue].append(classify)

paper_info=pd.DataFrame({'PaperID':IDs,'Title':titles,'PublishDate':dates,'PrimaryVenue':venues,'AIProb':classifies})
with open(os.path.join('..','dataset','paper_info.pkl'),'wb') as f:
    pickle.dump(paper_info,f)


IDs=list()
names=list()
numbers=list()
AI_probs=list()

for VenueID,paper_values in tqdm(venue_paper_count.items()):
    IDs.append(VenueID)
    try:
        name=source_name[VenueID]
        number=len(paper_values)
        AI_prob=np.mean(paper_values)
    except:
        continue

    names.append(name)
    numbers.append(number)
    AI_probs.append(AI_prob)
        
venue_info=pd.DataFrame({'VenueID':IDs,'Name':names,'NumberOfPapers':numbers,'AvgAIProb':AI_probs})
with open(os.path.join('..','dataset','venue_info.pkl'),'wb') as f:
    pickle.dump(venue_info,f)