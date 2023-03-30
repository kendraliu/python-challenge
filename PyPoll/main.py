import csv
import os

cwd = os.getcwd()
data = cwd + "/python-challenge/PyPoll/Resources/election_data.csv"
outputpath = cwd + "/python-challenge/PyPoll/analysis/PyPollAnalysis.txt"

ballotid = []
candidate = []
votes = 0
eachvote = []
votespercent = []

with open(data) as csvfile:
    polldata = csv.reader(csvfile)
    next(polldata)
    for row in polldata:
        ballotid.append(row[0])
        #for i in range(len(candidate)):
        if row[2] not in candidate:
            candidate.append(row[2])
            eachvote.append(0)
            votespercent.append(0)
        for j in range(len(candidate)):
            if row[2]==candidate[j]:
                eachvote[j]=eachvote[j]+1
    totalvotes = len (ballotid)
    for i in range(len(candidate)):
        votespercent[i] = str(round(eachvote[i]/sum(eachvote)*100, 3)) + "%"
    maxvote = max(eachvote)
    winner = candidate[eachvote.index(maxvote)]
    print(f"Election Results\n-------------------------\nTotal Votes: {totalvotes}\n-------------------------")
    for k in range(len(candidate)):
        print(f"{candidate[k]}: {votespercent[k]} ({eachvote[k]})")
    print(f"-------------------------\nWinner: {winner}\n-------------------------")

with open(outputpath, "w") as text:
    text.write(f"Election Results\n-------------------------\nTotal Votes: {totalvotes}\n-------------------------\n")
    for k in range(len(candidate)):
        text.write(f"{candidate[k]}: {votespercent[k]} ({eachvote[k]})\n")
    text.write(f"-------------------------\nWinner: {winner}\n-------------------------")
