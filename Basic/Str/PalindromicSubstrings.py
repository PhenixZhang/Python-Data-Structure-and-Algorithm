
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


def CS(s):
    cnt = 0

    def countSubstrings(s):
        for i in range(len(s)):
            extendSubStrings(s,i,i)
            extendSubStrings(s,i,i+1)
        return cnt


    def extendSubStrings(s,start,end):
        nonlocal cnt
        while(start >=0 and end < len(s) and s[start]==s[end]):
            start -= 1
            end += 1
            cnt += 1

    return countSubstrings(s)



# 拓展  求长回文子字符串



def CS2(s):
    result = ''

    def countSubstrings(s):
        for i in range(len(s)):
            extendSubStrings(s,i,i)
            extendSubStrings(s,i,i+1)
        return result


    def extendSubStrings(s,start,end):
        nonlocal result
        while start >=0 and end < len(s) and s[start]==s[end]:

            if len(s[start:end+1]) > len(result):
                result = s[start:end+1]
            start -= 1
            end += 1

    return countSubstrings(s)






if __name__ == "__main__":
    s = 'aaa'
    print(CS(s))

    print(CS2(s))
    s = 'aabcdedcb'
    print(CS2(s))

    s = 'aabcdeedcb'
    print(CS2(s))
