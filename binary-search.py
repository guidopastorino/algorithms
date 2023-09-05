# Returns the position of the element in the list, otherwise returns -1
def binarySearch(lst: list, target: int) -> int:
    l, u = 0, len(lst) - 1
    
    while l <= u:
        mid = (l+u) // 2
        
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            l = mid + 1
        else:
            u = mid - 1
            
    return -1