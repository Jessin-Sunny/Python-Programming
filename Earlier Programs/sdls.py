
from prettytable import PrettyTable,from_csv
table = PrettyTable(['Squad No','Player','Date of birth / Age','Club',
'Height','Foot','International Matches','Goals','Debut','Market Value(in rupees)'])
f=open('squaddetails.csv','r')

mytable=from_csv(f)
print(mytable)
