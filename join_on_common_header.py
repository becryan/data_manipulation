# joins multiple spreadsheets based on common headers.


import pandas as pd
import glob
interesting_files = glob.glob("CSVFILES/*.csv")
df_list = []
for filename in sorted(interesting_files):
    print(filename)
    df_list.append(pd.read_csv(filename,sep='|'))
full_df = pd.concat(df_list)

full_df.to_csv('output.csv',sep='|')