import csv

csv_reader = csv.DictReader(open('Resources/election_data.csv'))
My_report = open('analysis/election_poll.txt','w')

total = 0 
can_list = []
candidates = {}
winner = ""
winning_count = 0

for row in csv_reader:

    total += 1
    candidate = row['Candidate']

    if candidate not in can_list:
        can_list.append(candidate)
        candidates[candidate] = 0

    candidates[candidate] += 1

output = (f'''
Election Results
-------------------------
Total votes: {total:,}
-------------------------
''')

for candidate in candidates:
    votes = candidates.get(candidate)
    vote_per = float(votes)/float(total) * 100

    if votes > winning_count:
        winning_count = votes
        winner = candidate 
    
    output += f'{candidate}: {votes/total*100:.3f}% ({votes:,})\n'

output += (f'''------------------------
"Winner" : {winner}
------------------------''')
print(output)
My_report.write(output)