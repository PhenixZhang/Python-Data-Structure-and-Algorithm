# 有序数组的 Two Sum

# Leetcode ：167. Two Sum II - Input array is sorted (Easy)

# Input: numbers=[2, 7, 11, 15], target=9
# Output: index1=0, index2=1



# 思路
# 如果两个指针指向元素的和 sum == target，那么得到要求的结果；
# 如果 sum > target，移动较大的元素，使 sum 变小一些；
# 如果 sum < target，移动较小的元素，使 sum 变大一些。



def twoSum(lst,target):
    result = []
    i = 0
    j = len(lst)-1
    while i < j:
        sum = lst[i] + lst[j]
        if sum == target:
            result.append((i,j))
            i += 1
        elif sum > target:
            j -= 1
        else :
            i += 1
    return result


def twoSum2(lst, target):
    indexForNum = dict()
    for i in range(len(lst)):
        if (target - lst[i]) in indexForNum:
            return [indexForNum.get(target-lst[i]), i]
        else:
            indexForNum[lst[i]] = i


# 延伸three sum

def threeSum(lst,target):
    result = []
    for i in range(len(lst)-2):
        j = i + 1
        k = len(lst) - 1
        target_temp = target - lst[i]
        while j < k:
            sum = lst[j] + lst[k]
            if sum == target_temp:
                result.append((i,j,k))
                j += 1
            elif sum > target_temp:
                k -= 1
            else :
                j += 1
    return result


# 延伸three sum closest

def threeSumClosest(lst,target):
    diff = 99999
    closest = 0
    for i in range(len(lst)-2):
        j = i+1
        k = len(lst)-1
        while j<k:
            sum = lst[i] + lst[j] + lst[k]
            if sum == target:
                return (i,j,k)
            elif sum > target:
                if sum - target < diff:
                    diff = sum - target
                    closest = sum
                k -= 1
            else :
                if target - sum < diff:
                    diff = target - sum
                    closest = sum
                j += 1
    return closest








if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 18
    print(twoSum(numbers,target))
    print(twoSum2(numbers, target))

    numbers = [1,2,3,4,5,6,7,8]
    target = 9
    print(twoSum(numbers,target))
    print(threeSum(numbers,target))

    print(threeSumClosest([1,3,5,7,9],10))