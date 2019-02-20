# -- coding:utf-8 --

# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to
# get a non-decreasing array.


# 题目描述：判断一个数组能不能只修改一个数就成为非递减数组。
#
# 在出现 nums[i] < nums[i - 1] 时，需要考虑的是应该修改数组的哪个数，
# 使得本次修改能使 i 之前的数组成为非递减数组，并且 不影响后续的操作 。
# 优先考虑令 nums[i - 1] = nums[i]，因为如果修改 nums[i] = nums[i - 1] 的话，
# 那么 nums[i] 这个数会变大，就有可能比 nums[i + 1] 大，从而影响了后续操作。
# 还有一个比较特别的情况就是 nums[i] < nums[i - 2]，只修改 nums[i - 1] = nums[i]
# 不能使数组成为非递减数组，只能修改 nums[i] = nums[i - 1]。


def checkPossibility(nums):
    cnt = 0
    for i in range(1,len(nums)):
        if cnt > 1:
            break
        if nums[i] >= nums[i-1]:
            continue
        cnt += 1
        if i-2 >= 0 and nums[i-2] > nums[i]:
            nums[i] = nums[i-1]
        else:
            nums[i-1] = nums[i]
    return cnt <= 1



if __name__ == "__main__":
    nums = [4,2,3]
    print(checkPossibility(nums))

    nums = [2,2,3,4,6,2,8]
    print(checkPossibility(nums))

    nums = [2,2,3,4,6,2,5,8]
    print(checkPossibility(nums))




