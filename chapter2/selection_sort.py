def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    result = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        result.append(arr.pop(smallest))
    return result


a = map(int, input().split())
inputarr = []
for ai in a:
    inputarr.append(ai)
print(selectionSort(inputarr))
