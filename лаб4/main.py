import pandas as pd
df = pd.read_csv('data.csv')
print(df)
names = ['IPhone 10',  'IPhone XS',  'IPhone 11',  'IPhone 11 PRO',   'IPhone 12']
def fun(row,name):
    return row['Вага']*row[name]
list_=[]
for i in range(len(names)):
    list_.append(round(sum(df.apply(fun,name=names[i], axis = 1)),2))
result = list(zip(names,list_))
result_df = pd.DataFrame(result,columns=['Параметр','Вага'])
print(result_df.sort_values(['Оцінка'], ascending=False))
print()
print(result_df.iloc[result_df['Оцінка'].idxmax()])