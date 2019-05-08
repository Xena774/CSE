import csv

profit_list = []

item_profit = {
    'Fruits': {
        'Entry': 0
    },
    'Clothes': {
        'Entry': 0
    },
    'Meat': {
        'Entry': 0
    },
    'Beverages': {
        'Entry': 0
    }
}


with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    for row in reader:
        if row[13] == "Total Profit":
            continue
        item = row[2]
        profit = float(row[13])
        if "Fruits" == item:
            profit_list.append(profit)
            total_profit = sum(profit_list)
    print(total_profit)
