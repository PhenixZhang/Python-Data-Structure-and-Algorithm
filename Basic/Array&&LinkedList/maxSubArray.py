# -- coding:utf-8 --

# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:

# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


# 思路
# 设sumArr[i]为以第i个元素结尾且和最大的连续子数组的和。假设对于元素i，所有以它前面的元素结尾的最大连续子数组和都已经求得，
# 那么以第i个元素结尾且和最大的连续子数组实际上，要么是以第i-1个元素结尾且和最大的连续子数组加上这个元素，
# 要么是只包含第i个元素，即sumArr[i] = max(sumArr[i-1] + a[i], a[i])。
# 可以通过判断sumArr[i-1] + a[i]是否大于a[i]来做选择，而这实际上等价于判断sumArr[i-1]是否大于0。
# 另外只需要再多增加一个变量来记录最大的子数组和


def maxSubArray(lst):
    sumArr = [lst[0]]
    maxArr = lst[0]
    for i in range(1,len(lst)):
        sumArr.append(max(sumArr[i-1]+lst[i], lst[i]))
        if maxArr < sumArr[i]:
            maxArr = sumArr[i]
    return maxArr



# 思路2
# 当我们加上一个正数时，和会增加；当我们加上一个负数时，和会减少。
# 如果当前得到的和是个负数，那么这个和在接下来的累加中应该抛弃并重新清零，
# 不然的话这个负数将会减少接下来的和

def maxSubArray2(lst):
    current = lst[0]
    maxArr = lst[0]

    for i in range(1,len(lst)):
        if current < 0:
            current = lst[i]
        else:
            current += lst[i]
        if maxArr < current:
            maxArr = current
    return maxArr

if __name__ == "__main__":
    alist = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(alist))
    print(maxSubArray2(alist))



