
import pandas as pd
import sys
if len(sys.argv) <4:
    print ('Syntax: python ./src/donation-analytics.py ./input/itcont.txt ./input/percentile.txt ./output/repeat_donors.txt')
    exit()

def gainData(filepath):
    df = pd.read_csv(filepath,sep = ';',index_col = False)
    return df

def count(df,string):
    df_cer = df[df['CASE_STATUS']=='CERTIFIED']
    count = df_cer.groupby([string],as_index=False)[string].agg({'NUMBER_CERTIFIED_APPLICATIONS':'count'})
    count = count.sort_values(by = 'NUMBER_CERTIFIED_APPLICATIONS',ascending = False)
    count['PERCENRAGE'] = count['NUMBER_CERTIFIED_APPLICATIONS']/len(df_cer)
    count['PERCENRAGE'] = count['PERCENRAGE'].apply(lambda x: format(x,'0.1%'))
    if len(count['NUMBER_CERTIFIED_APPLICATIONS'].drop_duplicates()) >= 10:
        top_occ = count.loc[count['NUMBER_CERTIFIED_APPLICATIONS'].isin(count['NUMBER_CERTIFIED_APPLICATIONS'].drop_duplicates()[:10])]
    else:
        top_occ = count.loc[count['NUMBER_CERTIFIED_APPLICATIONS'].isin(count['NUMBER_CERTIFIED_APPLICATIONS'].drop_duplicates())]
    if string == 'SOC_NAME':
        name = 'TOP_OCCUPATIONS'
    else:
        name = 'TOP_STATES'
    top_occ.rename(columns={top_occ.columns[0]: name }, inplace=True)
    re = top_occ.sort_values(by = ['NUMBER_CERTIFIED_APPLICATIONS',name],ascending = [False,True])
    return re

#df = gainData(sys.argv[1])
df = gainData(sys.argv[1])
re_states = count(df,'WORKSITE_STATE')
re_occu = count(df,'SOC_NAME')
re_occu.to_csv(sys.argv[2],sep = ';',index = None)
re_states.to_csv(sys.argv[3],sep = ';',index = None )

    

