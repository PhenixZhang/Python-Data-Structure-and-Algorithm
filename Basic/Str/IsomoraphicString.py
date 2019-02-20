# 记录一个字符上次出现的位置，如果两个字符串中的字符上次出现的位置一样，那么就属于同构。
# 小写字母
# Given "egg", "add", return true.
# Given "foo", "bar", return false.
# Given "paper", "title", return true.


def isIsomorphic(s,t):

    preIndexOfs = [0] * 26
    preIndexOft = [0] * 26

    for i in range(len(s)):
        sc = s[i]
        tc = t[i]
        if preIndexOfs[ord(sc)-97] != preIndexOft[ord(tc)-97]:
            return False
        preIndexOfs[ord(sc)-97] = i+1
        preIndexOft[ord(tc)-97] = i+1

    return True



if __name__ == "__main__":
    s = 'egg'
    t = 'add'
    print(isIsomorphic(s,t))

    s = 'foo'
    t = 'bar'
    print(isIsomorphic(s,t))

    s = 'paper'
    t = 'title'
    print(isIsomorphic(s,t))
