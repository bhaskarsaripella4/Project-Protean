import pandas as pd
import numpy as np
#
# # to convert some boolean values into binary
# df["somecolumn"] = df["somecolumn"].astype(int)
#
# #to get names of columns in dataframe
# for col in data.columns:
#     print(col)
# #alternative methods
# list(data.columns)
# list(data.columns.values)
# sorted(data) #returns list of columns in sorted order
#
# df = pd.DataFrame(index=['a', 'b', 'c'], columns=['time', 'date', 'name'])
# df.iloc[0]


df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']})



