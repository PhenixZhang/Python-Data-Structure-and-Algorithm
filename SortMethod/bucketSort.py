# -- coding:utf-8 --

# Top K Frequent Elements (Medium)
# Given [1,1,1,2,2,3] and k = 2, return [1,2].



def topKfrequent(lst, k):
    # 构建一个字典，健是序列中的元素，值是元素在序列中出现的频率
    dct = {}
    for each in lst:
        dct[each] = dct.get(each,0)+1

    # 构建len(lst)+1个桶，桶的下标为频率，桶内存放在原序列中出现相同频率的元素
    bucket = [None] * (len(lst)+1)
    for key in dct.keys():
        freq = dct[key]
        if not bucket[freq]:
            bucket[freq] = []
        bucket[freq].append(key)

    # 按照从频率从高到低的顺序，依次取桶
    topK = []
    for i in range(len(bucket)-1,0,-1):
        if len(topK) >= k:
            break
        if bucket[i]:
            topK.extend(bucket[i])

    return topK


if __name__ == "__main__":
    alist = [1,1,1,2,2,3,4,4,4,4,4,4,5,5,8,8,8,8,8,8,8]
    topK = topKfrequent(alist,3)
    print(topK)



