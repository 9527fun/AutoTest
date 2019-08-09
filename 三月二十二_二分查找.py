def binary_search(alist,item):
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            return binary_search(alist[0, mid-1], item)
        else:
            return binary_search(alist[mid + 1, n - 1], item)

    return -1






