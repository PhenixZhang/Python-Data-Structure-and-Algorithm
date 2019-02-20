# -- coding:utf-8 --


def countingSort1(lst,maxvalue):
    # 构建一个数组，下标为原序列的元素，值为频率
    arr = [0] * (maxvalue+1)
    for each in lst:
        arr[each] += 1

    # 新建一个指针指向待插入数组的位置
    sortedInd = 0

    for i in range(len(arr)):
        # 检查数i是否存在于原序列中
        while arr[i]>0:
            lst[sortedInd] = i
            sortedInd += 1
            arr[i] -= 1


def countingSort2(lst,minvalue,maxvalue):
    # 构建一个数组，下标为（原序列元素值-序列元素的最小值），值为频率
    arr = [0] * (maxvalue - minvalue + 1)
    for each in lst:
        arr[each - minvalue] += 1

    sortedInd = 0

    for i in range(len(arr)):
        while arr[i]>0:
            lst[sortedInd] = i + minvalue
            sortedInd += 1
            arr[i] -= 1


def countingSort(lst):
    maxvalue = lst[0]
    minvalue = lst[0]

    for each in lst[1:]:
        if each > maxvalue:
            maxvalue = each
        if each < minvalue:
            minvalue = each

    arr = [0] * (maxvalue - minvalue + 1)
    for each in lst:
        arr[each - minvalue] += 1

    sortedInd = 0

    for i in range(len(arr)):
        while arr[i]>0:
            lst[sortedInd] = i + minvalue
            sortedInd += 1
            arr[i] -= 1



if __name__ == "__main__":
    alist = [4,5,6,7,5,4,3,4,5,6,8,0,3,4,5,3,9]
    # countingSort1(alist,9)
    # countingSort2(alist,0,9)
    countingSort(alist)
    print(alist)