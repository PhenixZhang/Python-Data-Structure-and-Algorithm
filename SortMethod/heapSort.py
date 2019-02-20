# -- coding:utf-8 --

# 树、二叉树、满二叉树、完全二叉树、搜索二叉树、平衡二叉树、堆
# heap: [root,rootLeft,rootRight,rootLeftLeft,rootLeftRight,...]
# 利用堆排序求序列中最大/小的几个数，可并行 # 赛马问题


def heapSort(lst):
    n = len(lst) - 1
    for i in range((n-1)//2,-1,-1):
        heapAdjust(lst,i,n)
    for i in range(n,0,-1):
        swap(lst,0,i)
        heapAdjust(lst,0,i-1)


def heapAdjust(lst,low,high):
    temp = lst[low]
    j = 2*low+1
    while j <= high:
        if j<high and lst[j] < lst[j+1]:
            j += 1
        if temp >= lst[j]:
            break
        lst[low] = lst[j]
        low = j
        j = 2*j + 1
    lst[low] = temp


def swap(lst,i,j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


if __name__ == "__main__":
    alist = [9,5,6,7,3,2,5,7,0,23,42,75,97,43,23,4,5,435,765,23]
    heapSort(alist)
    print(alist)








