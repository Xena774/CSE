import csv

item_profit = {}
top_profit = 0

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    for row in reader:
        if row[13] == "Total Profit":
            continue
        item = row[2]
        Indv_profit = float(row[13])
        try:
            item_profit[item] += Indv_profit
        except KeyError:
            item_profit[item] = Indv_profit
            
    print(item_profit)
