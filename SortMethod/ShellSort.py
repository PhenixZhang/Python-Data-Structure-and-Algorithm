# -- coding:utf-8 --

def shellSort(lst,delta):
    for deltaK in delta:
        shellInsert(lst,deltaK)


def shellInsert(lst,deltaK):
    # 获取序列长度
    length = len(lst)
    # 类似插入排序，只不过这次的跳跃间隔为deltaK
    for i in range(deltaK,length,1):
        if lst[i-deltaK] > lst[i]:
            current = lst[i]
            preInd = i - deltaK
            while preInd >= 0 and lst[preInd] > current:
                lst[preInd + deltaK] = lst[preInd]
                preInd -= deltaK
            lst[preInd + deltaK] = current


if __name__ == "__main__":
    alist = [9,5,6,7,3,2,5,7,0,23,42,75,97,43,23,4,5,435,765,23]
    # delta初始值设置为待排序序列长度的一半，依次递减到1为止
    delta = range(10,0,-1)
    shellSort(alist,delta)
    print(alist)