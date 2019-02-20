# 回溯

# Restore IP Addresses(Medium)

# Given "25525511135",
# return ["255.255.11.135", "255.255.111.35"].
# 主函数
def restoreIpAddresses(s):
    '''
    s：输入字符串
    addresses:目标输出
    tempAddress:中间件
    '''
    addresses = []
    tempAddress = ''
    doRestore(0,tempAddress,addresses,s)
    return addresses

# 递归回溯函数
def doRestore(k, tempAddress, addresses, s):
    if k == 4 or len(s) == 0:               # 边界条件
        if k == 4 and len(s) == 0:
            addresses.append(tempAddress)
        return
    i = 0
    while i < len(s) and i <= 2:            #
        if i != 0 and s[0] == '0':
            break
        part = s[:i+1]
        if int(part) <= 255:
            if len(tempAddress) != 0:
                part = "." + part
            tempAddress += part
            doRestore(k+1,tempAddress,addresses,s[i+1:])
            tempAddress = tempAddress[:len(tempAddress)-len(part)]
        i += 1

if __name__ == "__main__":
    s = "25525511135"
    print(restoreIpAddresses(s))





