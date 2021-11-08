def type_values_in_list(var_list):
    new_list = []
    for item in var_list:
        item = int(item)
        new_list.append(item)
    return new_list


def min_max(var_list):
    min_in_list = var_list[0]
    max_in_list = var_list[0]
    for item in var_list:
        if item < min_in_list:
            min_in_list = item
        if item > max_in_list:
            max_in_list = item
    return min_in_list, max_in_list


def avg_from_list(var_list):
    sum_from_list = 0
    for item in var_list:
        sum_from_list += item
    average = sum_from_list / len(var_list)
    return average


if __name__ == "__main__":
    my_list = []
    for i in range(5):
        digit = input("Give a digit for a list: ")
        my_list.append(digit)
    print(my_list)
    my_list = type_values_in_list(my_list)
    print(my_list)
    min_number, max_number = min_max(my_list)
    print(f'Average from list is {avg_from_list(my_list)}')
    print(f"Min is equal {min_number}")
    print(f"Max is equal {max_number}")
