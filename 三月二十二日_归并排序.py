def merge_sort(alist):
    """ 归并排序 """
    n = len(alist)
    if n <= 1:  # 递归拆分成一个数字
        return alist
    mid = n // 2
    left_li = merge_sort(alist[0:mid])  # 左面的有序序列
    right_li = merge_sort(alist[mid:])  # 右面的有序序列
    left_point, right_point = 0, 0      # 定义两个指针
    result = []                         # 定义一个空链表装结果

    while left_point <= len(left_li) and right_point <= len(right_li):
        '''循环的条件：指针数字小于该表的长度'''
        if left_li[left_point] < right_li[right_point]:  # 左面的列表和右面的列表比大小，谁小谁加入result[]
            result.append(left_li[left_point])
            left_point += 1
        else:
            result.append(right_li[right_point])
            right_point += 1
    result += left_li[left_point:]    # 加入剩下的列表
    result += right_li[right_point:]  # 加入剩下的列表
    return result  # 返回结果


if __name__ == "__main__":
    li = [23, 444, 22, 2, 3, 4, 6, 7, 12123]
    print(li)
    sorted_li = merge_sort(li)
    print(sorted_li)
create database python charset=utf8
