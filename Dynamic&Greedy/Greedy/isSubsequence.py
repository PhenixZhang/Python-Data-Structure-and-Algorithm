# -- coding:utf-8 --


# s = "abc", t = "ahbgdc"
# Return true.

# 贪心：从前面开始匹配，给后面的字母留下更大的搜索空间

def isSubsequence(s, t):
    index = -1
    for each in s:
        index = t.find(each, index+1)
        if index == -1:
            return False
    return True


if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    print(isSubsequence(s, t))

    s = "abb"
    t = "ahbgdc"
    print(isSubsequence(s, t))




