# 计算一组字符集合可以组成的回文字符串的最大长度
# 小写字母
# Input : "abccccdd"
# Output : 7
# Explanation : One longest palindrome that can be built is "dccaccd", whose length is 7.



def longestPalindrome(s):
    cnts = [0] * 26
    for each in s:
        cnts[ord(each)-97] += 1

    palindrome = 0
    for cnt in cnts:
        palindrome += (cnt//2) * 2

    if palindrome < len(s):
        palindrome += 1

    return palindrome


if __name__ == "__main__":
    s = 'abccccdd'
    print(longestPalindrome(s))











