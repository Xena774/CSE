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
        unit_price = float(row[9])
        unit_cost = float(row[10])

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

        if item_profit[item]/units_dict[item] > units:
            units = round(item_profit[item]/units_dict[item], 2)

    for key, value in item_profit.items():
        if value == top_item_profit:
            print(key)

    for key, value in region_profit.items():
        if value == top_region_profit:
            print(key)

    for key, value in units_dict.items():
        print(round(item_profit[item] / value, 2))
        print(units)
        if round(value / units_dict[item], 2) == units:
            print(key + "!!!!!!!!!!!!!!!!!!")
