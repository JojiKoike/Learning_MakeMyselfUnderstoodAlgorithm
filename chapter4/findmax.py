def find_max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    else:
        sub_max = max(list[1:])
        return list[0] if list[0] > sub_max else sub_max

print(find_max([3, 4, 2, 1, 5]))
