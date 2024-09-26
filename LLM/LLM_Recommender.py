import pandas as pd
import numpy as np
import os
os.chdir(r'F:')
os.getcwd()
import time
from datetime import datetime
import json





groc_data = pd.read_csv(r'F:\Courses\MyKaggle Notebooks\Groceries_dataset.csv')

print(groc_data.head(10))
# print(groc_data.Date)

grouped_data = groc_data.groupby(by=['Date','Member_number'], as_index=False)['itemDescription'].apply(lambda x: ','.join(x))
# grouped_data = groc_data.groupby(by=['Date','Member_number'], as_index=False).agg({'itemDescription': ','.join})
print(grouped_data[['Member_number','Date','itemDescription']])
champ= grouped_data.loc[grouped_data['Member_number']==2851]



