# -- coding:utf-8 --.

def insertSort(lst):
    # 获取序列长度
    length = len(lst)
    # 循环控制起点及终点
    for i in range(1,length):
        # 将待比较的位置用preInd指向
        preInd = i - 1
        # 将未排序区域的第一个数用current变量保存
        current = lst[i]
        while preInd >=0 and lst[preInd] > current:
            lst[preInd+1] = lst[preInd]
            preInd -= 1
        lst[preInd+1] = current


def biInsertSort(lst):
    # 获取序列长度
    length = len(lst)
    # 控制循环起点及终点
    for i in range(1,length):
        # 设置二分查找的上限
        hi = i-1
        # 设置二分查找的下限
        lo = 0
        # 将未排序区的第一个数用current变量保存
        current = lst[i]
        # 通过二分查找找到合适的插入位置为hi+1
        while lo <= hi:
            mid = int((lo+hi)/2)
            if lst[mid] > current:
                hi = mid -1
            else:
                lo = mid + 1
        # 将排好序区域的位置依次挪动
        for j in range(i-1,hi,-1):
            lst[j+1] = lst[j]
        # 将待插入数插入到正确的位置
        lst[hi+1] = current


if __name__ == "__main__":
    alist = [9,5,6,7,3,2,5,7,0]
    # insertSort(alist)
    biInsertSort(alist)
    print(alist)


