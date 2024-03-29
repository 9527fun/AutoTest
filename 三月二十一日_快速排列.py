def quick_sort(alist, first, last):
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value
    quick_sort(alist, first, low - 1)
    quick_sort(alist, low + 1, last)


if __name__ == "__main__":
        li = [23, 444, 22, 2, 3, 4, 6, 7, 12123]
        print(li)
        quick_sort(li, 0, len(li)-1)
        print(li)