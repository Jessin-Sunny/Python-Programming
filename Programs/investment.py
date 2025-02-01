amount = float(input("Enter the Amount: "))
year = int(input("Enter the number of years: "))
rate = float(input("Enter the rate as a %: "))

startBalance = amount
total = 0
print("%4s%18s%10s%16s"%("Year", "Starting Balance", "Interest", "Ending Balance"))
for i in range(year):
    interest = startBalance*(rate/100)
    endBalance = startBalance + interest
    print("%4d%18.2f%10.2f%16.2f" %(i, startBalance, interest, endBalance))
    startBalance = endBalance
    total += interest
print("Ending Balance: $%0.2f" % endBalance)
print("Total interest earned: $%0.2f" % total)
