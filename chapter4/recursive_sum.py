def recursive_sum(list):
    if not list:
        return 0
    return list[0] + sum(list[1:])


print(recursive_sum([1,2,3,4]))
