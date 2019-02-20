# -- coding:utf-8 --
from SortMethod.mergeSort import mergeSort

def binSearch(lst,target):
    length = len(lst)
    low = 0
    high = length - 1
    while low <= high:
        mid = (low+high)//2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            high = mid -1
        else :
            low = mid + 1
    return -1


if __name__ == "__main__":
    alist = [4,3,6,7,8,9,3,2,54,7]
    mergeSort(alist)
    print(alist)
    print(binSearch(alist,54))










