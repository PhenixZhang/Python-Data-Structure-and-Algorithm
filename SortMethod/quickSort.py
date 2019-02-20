# -- coding:utf-8 --


def quickSort(lst):
    length = len(lst)
    recurQuickSort(lst,0,length-1)


def recurQuickSort(lst,low,high):
    if low < high:
        pa = partition(lst,low,high)
        recurQuickSort(lst,low,pa-1)
        recurQuickSort(lst,pa+1,high)


def partition(lst,low,high):
    # 设置比较基准为序列片段的第一个数
    pivot = lst[low]
    # 通过两个指针从两头往中间扫，并返回分界点
    while low < high:
        while low<high and lst[high] >= pivot:
            high -= 1
        lst[low] = lst[high]
        while low<high and lst[low] <= pivot:
            low += 1
        lst[high] = lst[low]

    lst[low] = pivot
    return low


if __name__ == "__main__":
    alist = [9,5,6,7,3,2,5,7,0,23,42,75,97,43,23,4,5,435,765,23]
    quickSort(alist)
    print(alist)




