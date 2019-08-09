def insert_sort(alist):
    n = len(alist)
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i - 1] > alist[i]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1
            else:
                break


if __name__ == "__main__":
    li = [23, 444, 22, 2, 3, 4, 6, 7, 12123]
    print(li)
    insert_sort(li)
    print(li)
