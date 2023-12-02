from prettytable import PrettyTable,from_csv

f=open('squaddetails.csv','r')

mytable=from_csv(f)
print(mytable)
