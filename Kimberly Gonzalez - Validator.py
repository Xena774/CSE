test_num = "7555330005450890"


def reverse_it(list):
    return list[::-1]


def validate(num: str):
    if len(test_num) == 16:
        num_list = list(test_num)
        last_num = num_list[len(num_list) - 1]
        new_list = reverse_it(num_list)
        new_list.remove(last_num)
        for index in range(len(new_list)):
            int_version = int(new_list(index))
            if index % 2 == 0:
                a = int_version * 2
                if a > 9:
                    int_version = a - 9

        print(new_list)


validate(test_num)
