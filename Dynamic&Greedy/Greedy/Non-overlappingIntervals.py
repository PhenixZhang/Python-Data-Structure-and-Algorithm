# -- coding:utf-8 --

# Input: [ [1,2], [1,2], [1,2] ]
#
# Output: 2
#
# Explanation: You need to remove two [1,2]
# to make the rest of intervals non-overlapping.



# Input: [ [1,2], [2,3] ]
#
# Output: 0
#
# Explanation: You don't need to
# remove any of the intervals since they're already non-overlapping.

# 题目描述：计算让一组区间不重叠所需要移除的最少区间个数。
#
# 先计算最多能组成的不重叠区间个数，然后用区间总个数减去不重叠区间的个数。
#
# 在每次选择中，区间的结尾最为重要，选择的区间结尾越小，留给后面的区间的空间越大，
# 那么后面能够选择的区间个数也就越大。
#
# 按区间的结尾进行排序，每次选择结尾最小，并且和前一个区间不重叠的区间。



def eraseOverlapIntervals(intervals):
    if len(intervals) == 0:
        return 0

    intervals = sorted(intervals, key = lambda lst: lst[1])
    cnt = 1
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            continue
        end = intervals[i][1]
        cnt += 1
    return len(intervals) - cnt


if __name__ == "__main__":
    intervals = [[1,2],[1,2],[1,2]]
    print(eraseOverlapIntervals(intervals))






