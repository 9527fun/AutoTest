def fibo (num):
    num_list = [0,1]
    for i in range(num-2):
        num_list.append(num_list[-2]+num_list[-1])
    return num_list

fibo(9)







