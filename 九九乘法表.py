row = 1
while row < 10:
    j = 1
    while j <= row:
        print("%d * %d = %d\t" % (row, j, j * row), end="")
        j += 1
    print()
    row += 1
