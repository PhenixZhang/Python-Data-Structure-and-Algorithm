# -- coding:utf-8 --


def selectSort(lst):
    # 获取序列长度
    length = len(lst)
    # 两层循环，外层控制内层的起点
    for i in range(length-1):
        minInd = i
        for j in range(i+1,length):
            if lst[j] < lst[minInd]:
                minInd = j
        swap(lst,i,minInd)


def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


if __name__ == "__main__":
    alist = [9,5,6,7,3,2,5,7,0]
    selectSort(alist)
    print(alist)