# 两个字符串包含的字符是否完全相同
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.


def VA(s,t):
    cnts = [0] * 26
    for each in s:
        cnts[ord(each)-97] += 1

    for each in t:
        cnts[ord(each) - 97] -= 1

    for each in cnts:
        if each != 0:
            return False
    return True


if __name__ == "__main__":
    s = 'anagram'
    t = 'nagaram'
    print(VA(s,t))
    
    s = 'rat'
    t = 'cat'
    print(VA(s,t))