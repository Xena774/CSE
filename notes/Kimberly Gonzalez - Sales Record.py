import csv

item_profit = {}
region_profit = {}
units_dict = {}
top_item_profit = 0
top_region_profit = 0
units = 0

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    for row in reader:
        if row[13] == "Total Profit":
            continue
        item = row[2]
        Indv_profit = float(row[13])
        region = row[0]
        units_sold = int(row[8])

        try:
            item_profit[item] += Indv_profit
            region_profit[region] += Indv_profit
            units_dict[item] += units_sold

        except KeyError:
            item_profit[item] = Indv_profit
            region_profit[region] = Indv_profit
            units_dict[item] = units_sold

        if item_profit[item] > top_item_profit:
            top_item_profit = item_profit[item]

        if region_profit[region] > top_region_profit:
            top_region_profit = region_profit[region]

    for key, value in item_profit.items():
        if value == top_item_profit:
            print("The most profitable item is %s." % key)

    for key, value in region_profit.items():
        if value == top_region_profit:
            print("The most profitable region is %s" % key)

    for key, value in units_dict.items():
        if item_profit[key] / value > units:
            units = item_profit[key] / value

    for key, value in units_dict.items():
        if item_profit[key] / value == units:
            print("The most profitable per unit is %s!!!" % key)
