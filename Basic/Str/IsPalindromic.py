# 判断回文字符串


def isPalindromic(s):
    endind = len(s) // 2
    for i in range(endind):
        if s[i] != s[len(s)-i-1]:
            return False
    return True



# 拓展  如何判断一个数是否为回文数


def isPalindromeNum(x):
    if x == 0:
        return True
    if x<0 or x % 10 == 0:
        return False

    right = 0
    while x>right:
        right = right * 10 + x % 10
        x = x//10

    return x == right or x == right // 10







if __name__ == "__main__":
    s = 'abcddcba'
    print(isPalindromic(s))

    s = 'abcdxdcba'
    print(isPalindromic(s))

    s = 'abcdxydcba'
    print(isPalindromic(s))
    


    print(isPalindromeNum(252))