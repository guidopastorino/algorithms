def quickSort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for element in arr[:-1]:
        if element <= pivot:
            left.append(element)
        else:
            right.append(element)

    return quickSort(left) + [pivot] + quickSort(right)


arr = [9,6,3,1,4,7]
sortedArr = quickSort(arr)
print(sortedArr)