def select_sort(alist):
    n = len(alist)
    for j in range(0, n-1):
        min_index = j
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]
        


if __name__ == "__main__":
    li = [123, 444, 22, 2, 3, 4, 6, 7, 12123]
    print(li)
    select_sort(li)
    print(li)
