# 参考 https://www.cnblogs.com/yjiyjige/p/3263858.html
# http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html


# partialtable的意义是：当第i号位元素不匹配，而前面的均匹配的时候，下次移动该移动到的索引位
# next[0] = -1
# next[1] = 0 非0号位的元素不匹配时，最远移动到0位
# next[j] = k, if a[j] == a[k]: next[j+1] = k + 1 else: k = next[k]
def getPartialTable(a):
    al = len(a)
    next = [0] * al
    next[0] = -1
    k = -1
    j = 0
    while j < al-1:
        if k == -1 or a[j] == a[k]:
            j += 1
            k += 1
            next[j] = k
        else:
            k = next[k]
    return next



def KmpSearch(a,b):
    next = getPartialTable(b)
    i = j = 0
    al = len(a)
    bl = len(b)
    while i < al and j < bl:
        if j == -1 or a[i] == b[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == bl:
        return i-j
    else:
        return -1



if __name__ == "__main__":
    a = 'ABABCABDABBGAFDSBVSABDABB'
    b = 'ABDABB'
    print(getPartialTable(b))
    print(KmpSearch(a,b))
