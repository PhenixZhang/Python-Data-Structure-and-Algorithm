# 回溯

#     1:O_O    2:abc     3:def
#     4:ghi    5:jkl     6:mno
#     7:pqrs   8:tuv     9:wxyz
#     *:+      0:blank   shift:#

#输入输出要求
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

# 电话键盘
Keys = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
# 主函数
def letterCombinations(digits):
    combinations = []   # 目标输出
    if digits is None or len(digits) == 0:  # 特殊判断
        return combinations
    doCombinations('',combinations,digits) 
    return combinations

# 回溯递归函数
def doCombinations(prefix,combinations,digits):
    if len(prefix) == len(digits):      # 边界条件
        combinations.append(prefix)
        return
    curDigits = int(digits[len(prefix)])
    letters = Keys[curDigits]
    for c in letters:
        prefix += c
        doCombinations(prefix,combinations,digits)
        prefix = prefix[:-1]

if __name__ == "__main__":
    digits = "23"
    print(letterCombinations(digits))