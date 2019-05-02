import csv


def reverse_it(list):
    return list[::-1]


def validate(num: str):
    if len(num) != 16:
        return False
    num_list = list(num)
    last_num = int(num_list[len(num_list) - 1])
    num_list.pop(15)
    new_list = reverse_it(num_list)
    for index in range(len(new_list)):
        new_list[index] = int(new_list[index])
        if index % 2 == 0:
            new_list[index] *= 2
            if new_list[index] > 9:
                new_list[index] -= 9
    list_sum = sum(new_list)
    if list_sum % 10 == last_num:
        return True
    else:
        return False


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", "w", newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")
        for row in reader:
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)
print("Done")
