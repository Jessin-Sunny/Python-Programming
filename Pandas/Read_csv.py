import pandas as pd
df = pd.read_csv('c:/My/RIT/S6/Programming with Python/Module 5/Programs/students.csv')
#print all student details
print(df)
#display first 5 records
print(df.head(5))
#names in ascending order of name
print(df.sort_values(by='Name',ascending=True)['Name'])
#name of student with highest grade
print(df.at[df['Grade'].idxmax(),'Name'])
#male student names
print(df[df['Gender'] == 'M']['Name'])
