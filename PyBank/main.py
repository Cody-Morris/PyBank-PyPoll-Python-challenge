import csv

csv_reader = csv.DictReader(open('Resources/budget_data.csv'))
My_report = open('analysis/budget_report.txt','w')

months = 0
total = 0
prev_rev = 867884
total_chg = 0
Greatinc = 0
Greatdec = 0

for row in csv_reader:
  #determine number of months & total
    months += 1
    rev =  float(row['Profit/Losses'])
    total += rev

    change = rev - prev_rev
    total_chg += change
    prev_rev = rev

    if change > Greatinc:

        Greatinc = change
        Greatincmonth = row['Date']
    
    if change < Greatdec:

        Greatdec = change
        Greatdecmonth = row['Date']

output = (f'''Financial Analysis
  ----------------------------
  Total Months: {months}
  Total: ${total:,.2f}
  Average  Change: ${total_chg/(months-1):,.2f}
  Greatest Increase in Profits: {Greatincmonth} ({Greatinc:,.0f})
  Greatest Decrease in Profits: {Greatdecmonth} ({Greatdec:,.0f})''')

print(output)
My_report.write(output)