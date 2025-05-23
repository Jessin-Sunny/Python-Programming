import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('c:/My/RIT/S6/Programming with Python/Module 5/Programs/student.csv')
print(df)
print(df.describe())
print(df.columns)
print(df.size)
print(df.dtypes)
print(df.shape)
print(df.index, len(df.index))
print(df['Mark'].sum())
print(df['Mark'].mean())
print(df['Mark'].min())
print(df['Mark'].max())
print(df['Mark'].std())
print(df.head(2))
print(df.tail(2))
print(df[0:3])
print(df[df['Mark'] > 40])
print(df.iloc[0:3,[0,2]])
print(df.sort_values(by = 'Mark', ascending = False))
print(df.sort_values(by='Mark', ascending=False).mode())
print(df.sort_values(by='Mark', ascending=False).median())
print(df['Mark'].agg(['min','max','mean']))
print(df.groupby('Mark')['Mark'].mean())
plt.hist(df['Mark'])
plt.show()
plt.scatter(df['Name'], df['Mark'])
plt.show()
print(df.iat[4,3])
print(df.at[0,'Name'])
print(df['Mark'].nunique())
print(df['Mark'].unique())
print(df.query('Mark>40'))
print(df.where(df['Mark'] > 40))