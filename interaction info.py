file_path = 'Grocery_and_Gourmet_Food_5.json'
fin = open(file_path, 'r')

df = {}
useless_col = ['reviewerName','reviewText','unixReviewTime','summary'] # 不想要的字段
i = 0
for line in fin:
    d = eval(line)
    for s in useless_col:
        if s in d:
            d.pop(s)
    df[i] = d 
    i += 1
df = pd.DataFrame.from_dict(df, orient='index')
df.to_csv('Grocery_and_Gourmet_Food_5.csv',index=False)

