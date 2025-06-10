def binarySearch(list, x) -> bool:
    list = sorted(list)
    lo = 0
    hi = len(l)-1

    while lo <= hi:
        mid = (lo + hi) // 2
        if list[mid] == x:
            return True
        elif x < list[mid]:
            hi = mid - 1
        else:
            lo = mid + 1

    return False

print(binarySearch([3, 5, 7, 8, 9, 11, 12, 14, 12, 11], 5))