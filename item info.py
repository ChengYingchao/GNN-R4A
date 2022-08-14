import pickle
import pandas as pd

file_path = 'meta_Grocery_and_Gourmet_Food.json'
fin = open(file_path, 'r')

df = {}
useless_col = ['imUrl','salesRank','related','title','description']  # 不想要的字段
i = 0
for line in fin:
    d = eval(line)
    for s in useless_col:
        if s in d:
            d.pop(s)
    df[i] = d 
    i += 1
df = pd.DataFrame.from_dict(df, orient='index')
df.to_csv('meta_Grocery_and_Gourmet_Food.csv',index=False)

