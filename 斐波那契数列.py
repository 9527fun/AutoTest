def fibonacci(num):
    alist = [0, 1]
    for i in range(num - 2):
        alist.append(alist[-1]+alist[-2])
    print(alist[911])


fibonacci(920)
