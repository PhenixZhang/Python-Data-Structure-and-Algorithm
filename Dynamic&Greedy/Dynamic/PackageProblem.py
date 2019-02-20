# 有一个容量为 c 的背包，要用这个背包装下物品的价值最大，这些物品有两个属性：体积 w 和价值 v。
# 背包容量为c

# 0-1背包：每种物品只有一个
# 完全背包：每种物品有无限个
# 多重背包：每种物品都有个数限制（不局限于一个）

# 拓展 若要求恰好装满呢
import numpy as np


# 0-1 背包
def oneZeroPack(w,v,c):
    dp = np.zeros((len(w),(c+1)),dtype=np.int32)
    for i in range(len(w)):
        for j in range(c+1):
            if i == 0:
                dp[i][j] = v[i] if j >= w[i] else 0
            else:
                if j >= w[i]:
                    dp[i][j] = max(dp[i-1][j-w[i]]+v[i], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]

    return dp[-1][-1]


# 0-1 背包省空间的办法
def oneZeroPack2(w,v,c):
    dp = np.array([0]*(c+1),dtype=np.int32)
    for i in range(len(w)):
        for j in range(c,-1,-1):
            if j >= w[i]:
                dp[j] = max(dp[j-w[i]]+v[i], dp[j])

    return dp[-1]




# 完全背包
def completePack(w,v,c):
    dp = np.zeros((len(w),(c+1)),dtype=np.int32)
    for i in range(len(w)):
        for j in range(c+1):
            if j >= w[i]:
                dp[i][j] = max(dp[i][j-w[i]]+v[i], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]


# 完全背包省空间办法
def completePack2(w,v,c):
    dp = np.array([0] * (c + 1), dtype=np.int32)
    for i in range(len(w)):
        for j in range(c+1):
            if j >= w[i]:
                dp[j] = max(dp[j-w[i]]+v[i], dp[j])

    return dp[-1]



# 多重背包问题
# 多了一个参数n[] ，表示第i件物品最多有n[i]个可用
# 思路一：转化为0-1背包，将w与v拉长，但这样效率太低
# 思路二：考虑二进制的思想，我们考虑把第i种物品换成若干件物品，使得原问题中第i种物品可取的每种策略——取0..n[i]件——均能等价于取若干件代换以后的物品。
# 另外，取超过n[i]件的策略必不能出现。
#
# 方法是：将第i种物品分成若干件物品，其中每件物品有一个系数，
# 这件物品的费用和价值均是原来的费用和价值乘以这个系数。
# 使这些系数分别为1,2,4,...,2^(k-1),n[i]-2^k+1，
# 且k是满足n[i]-2^k+1>0的最大整数。例如，如果n[i]为13，
# 就将这种物品分成系数分别为1,2,4,6的四件物品。
#
# 分成的这几件物品的系数和为n[i]，表明不可能取多于n[i]件的第i种物品。
# 另外这种方法也能保证对于0..n[i]间的每一个整数，均可以用若干个系数的和表示。

#
# 这样就将第i种物品分成了O(log n[i])种物品，
# 将原问题转化为了复杂度为O(V*Σlog n[i])的01背包问题，是很大的改进。


def multiplePack(w,v,n,c):
    dp = np.array([0] * (c + 1), dtype=np.int32)
    for i in range(len(w)):
        if n[i] * w[i] >= c:
            # 转化为完全背包
            ######################
            for j in range(c+1):
                if j >= w[i]:
                    dp[j] = max(dp[j - w[i]] + v[i], dp[j])
            ######################
        else:
            amount = n[i]
            k = 1
            while k < amount:
                # 转化为0-1背包
                #########################################
                for j in range(c, -1, -1):
                        if j >= w[i]*k:
                            dp[j] = max(dp[j - w[i]*k] + v[i]*k, dp[j])
                #########################################

                amount -= k
                k = k*2

            # 转化为0-1背包
            #########################################
            for j in range(c, -1, -1):
                    if j >= w[i] * amount:
                        dp[j] = max(dp[j - w[i] * amount] + v[i] * amount, dp[j])
            #########################################
    return dp[-1]


# 写的好看一点
def multilePack2(w,v,n,c):

    def ZOP(weight,value,capacity,i,dp):
        for j in range(capacity,-1,-1):
            if j >= weight:
                dp[j] = max(dp[j-weight]+value, dp[j])

    def CP(weight,value,capacity,i,dp):
        for j in range(capacity+1):
            if j >= weight:
                dp[j] = max(dp[j-weight]+value, dp[j])

    def MP(weight,value,capacity,i,dp):
        amount = n[i]
        if weight * amount >= capacity:
            CP(weight,value,capacity,i,dp)
            return
        k = 1
        while k<amount:
            ZOP(weight*k,value*k,capacity,i,dp)
            amount -= k
            k = k*2
        ZOP(amount*weight,amount*value,capacity,i,dp)


    dp = np.array([0] * (c + 1), dtype=np.int32)
    for i in range(len(w)):
        MP(w[i],v[i],c,i,dp)

    return dp[-1]


if __name__ == "__main__":
    c = 10
    w = [2, 2, 6, 5, 4]
    v = [6, 3, 5, 4, 6]
    print(oneZeroPack(w,v,c))
    print(oneZeroPack2(w,v,c))

    print("------------------------------")
    print(completePack(w,v,c))
    print(completePack2(w,v,c))


    print("------------------------------")
    n = [1,2,1,2,1]
    print(multiplePack(w,v,n,c))
    print(multilePack2(w,v,n,c))

    print("------------------------------")
    n = [3, 2, 1, 2, 1]
    print(multiplePack(w,v,n,c))
    print(multilePack2(w,v,n,c))