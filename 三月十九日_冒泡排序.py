def dana(shuzi):
    input(int(shuzi))
    for i in (1,10,100,1000,10000,100000,1000000,10000000,100000000):
        re = shuzi  % i
        if re > 0 and re < 10:
            
