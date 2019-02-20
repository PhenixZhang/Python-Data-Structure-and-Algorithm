# -- coding:utf-8 --


def bubble(lst):
    # 获取序列长度
    length = len(lst)
    # 两层循环，外层控制深度，内层实现冒泡
    for i in range(length-1, 0, -1):
        # 设置哨兵
        flag = True
        for j in range(i):
            if lst[j] > lst[j+1]:
                swap(lst, j, j+1)
                flag = False
        if flag:
            break


def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


if __name__ == "__main__":
    alist = [9,5,6,7,3,2,5,7,0]
    bubble(alist)
    print(alist)















