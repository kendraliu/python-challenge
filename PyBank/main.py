import csv
import os

cwd = os.getcwd()

#pybank = "/Users/glory/Documents/Data Bootcamp/python-challenge/PyBank/Resources/budget_data.csv"
pybank = cwd + "/python-challenge/PyBank/Resources/budget_data.csv"
pybankoutput = cwd + "/python-challenge/PyBank/analysis/PyBankAnalysis.txt"

month=[]
money=[]
profitchange=[]

with open(pybank) as csvfile:
    budgetdata = csv.reader(csvfile, delimiter=",")
    next(budgetdata)  # skip the header row
    for row in budgetdata:
        month.append(row[0])
        money.append(row[1])
    #month.pop(0)
    #money.pop(0)
    numofmonths = len(month)
    for i in range(len(money)):
        money[i]=int(money[i])
    totalprofit = sum(money)
    
    for i in range(len(money)-1):
        profitchange.append(money[i+1] - money[i])
    averagechange = round(sum(profitchange)/len(profitchange),2)
    maxprofit = max(profitchange)
    minprofit = min(profitchange)
    maxmonth = month[profitchange.index(maxprofit)+1]
    minmonth = month[profitchange.index(minprofit)+1]
    print("Fianancial Analysis\n----------------------------")
    print(f"Total Months: {numofmonths}\nTotal: ${totalprofit}\nAverage Change: ${averagechange}\nGreatest Increase in Profits: {maxmonth} (${maxprofit})\nGreatest Decrease in Profits: {minmonth} (${minprofit})")

with open(pybankoutput, "w") as text:
    text.write(f"Fianancial Analysis\n----------------------------\nTotal Months: {numofmonths}\nTotal: ${totalprofit}\nAverage Change: ${averagechange}\nGreatest Increase in Profits: {maxmonth} (${maxprofit})\nGreatest Decrease in Profits: {minmonth} (${minprofit})")