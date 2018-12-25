def count_elements(list):
    if not list:
        return 0
    else:
        return 1 + count_elements(list[1:])


print(count_elements([1,2,3,4,5]))
