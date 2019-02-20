# 最长递增子序列
# 已知一个序列 {S1, S2,...,Sn}，取出若干数组成新的序列 {Si1, Si2,..., Sim}，
# 其中 i1、i2 ... im 保持递增，即新序列中各个数仍然保持原数列中的先后顺序，
# 称新序列为原序列的一个 子序列 。
#
# 如果在子序列中，当下标 ix > iy 时，S[ix] > S[iy]，称子序列为原序列的一个 递增子序列 。
#
# 定义一个数组 dp 存储最长递增子序列的长度，dp[n] 表示以 Sn 结尾的序列的最长递增子序列长度。
# 对于一个递增子序列 {Si1, Si2,...,Sim}，
# 如果 im < n 并且 S[im] < Sn，此时 {Si1, Si2,..., Sim, Sn}
# 为一个递增子序列，递增子序列的长度增加 1。
# 满足上述条件的递增子序列中，长度最长的那个递增子序列就是要找的，
# 在长度最长的递增子序列上加上 Sn 就构成了以 Sn 为结尾的最长递增子序列。
# 因此 dp[n] = max{ dp[i]+1 | Si < Sn && i < n} 。
#
# 因为在求 dp[n] 时可能无法找到一个满足条件的递增子序列，此时 {Sn} 就构成了递增子序列，
# 需要对前面的求解方程做修改，令 dp[n] 最小为 1，即：
# dp[n] = max(1, dp[i]+1|si<sn&&i<n)

import numpy as np


def lengthOfLIS(nums):
    n = len(nums)
    dp = np.zeros(n,dtype=np.int32)
    for i in range(n):
        maxl = 1
        for j in range(i):
            if nums[i] > nums[j]:
                maxl = max(maxl, dp[j]+1)
        dp[i] = maxl

    ret = 0
    for each in dp:
        if each > ret:
            ret = each
    return ret


# 以上解法的时间复杂度为 O(N2)，可以使用二分查找将时间复杂度降低为 O(NlogN)。
#
# 定义一个 tails 数组，其中 tails[i] 存储长度为 i + 1 的最长递增子序列的最后一个元素。对于一个元素 x，
#
# 如果它大于 tails 数组所有的值，那么把它添加到 tails 后面，表示最长递增子序列长度加 1；
# 如果 tails[i-1] < x <= tails[i]，那么更新 tails[i] = x。
# 例如对于数组 [4,3,6,5]，有：

# tails      len      num
# []         0        4
# [4]        1        3
# [3]        1        6
# [3,6]      2        5
# [3,5]      2        null

# tails[0] 存储的是长度为1的最长递增子序列的最后一个元素
# tails[1] 存储的是长度为2的最长递增子序列的最后一个元素
# 可以看出 tails 数组保持有序，因此在查找 Si 位于 tails 数组的位置时就可以使用二分查找。


def lengthOfLIS2(nums):
    n = len(nums)
    tails = np.zeros(n,dtype=np.int32)
    length = 0
    for num in nums:
        index = binarySearch(tails,length,num)
        tails[index] = num
        if index == length:
            length += 1
    return length


def binarySearch(tails, length, key):
    l = 0
    h = length
    while l < h:
        mid = l + (h-l)//2
        if tails[mid] == key:
            return mid
        elif tails[mid] > key:
            h = mid
        else:
            l = mid + 1
    return l



if __name__ == "__main__":
    nums = [11,10,4,6,7,4,9,0,2]
    print(lengthOfLIS(nums))
    print(lengthOfLIS2(nums))


