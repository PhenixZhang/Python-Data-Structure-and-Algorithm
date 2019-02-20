# -- coding:utf-8 --


def mergeSort(lst):
    low = 0
    high = len(lst)-1
    recurMergeSort(lst,low,high)


def recurMergeSort(lst,low,high):
    if low < high:
        recurMergeSort(lst,low,(low+high)//2)
        recurMergeSort(lst,1+(low+high)//2,high)
        merge(lst,low,(low+high)//2,high)


def merge(lst, p, q, r):
    # 待合并的区间下标为[p..q]以及[q+1..r]
    s = p
    t = q+1
    b = []
    while s <= q and t <= r:
        if lst[s] <= lst[t]:
            b.append(lst[s])
            s += 1
        else :
            b.append(lst[t])
            t += 1

    # 情形一：若左边序列没有被耗尽
    while s <= q:
        b.append(lst[s])
        s += 1
    # 情形二：若右边序列没有被耗尽
    while t <= r:
        b.append(lst[t])
        t += 1
    # 将排序好的片段覆盖掉原序列
    for i in range(len(b)):
        lst[p+i] = b[i]


if __name__ == "__main__":
    alist = [9,5,6,7,3,2,5,7,0,23,42,75,97,43,23,4,5,435,765,23]
    mergeSort(alist)
    print(alist)



