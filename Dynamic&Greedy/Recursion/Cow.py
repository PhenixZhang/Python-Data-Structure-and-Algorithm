# -- coding:utf-8 --

# 在农场中，奶牛家族是一个非常庞大的家族，对于家族中的母牛，从它出生那年算起，第三年便能成熟，
# 成熟的母牛每年可以生出一只小母牛。即母牛从出生开始的第三年便能做妈妈。
# 最开始农场只有一只母牛，它从第二年开始生小母牛。
# 请回答第n年的母牛总数


# 1 2 3 4 6 9


def solution(year):

    class LittleCow():
        def __init__(self,age):
            self.age = age

        def getAge(self):
            return self.age

        def setAge(self,age):
            self.age = age

        def growUp(self, farm):
            self.age += 1
            if self.age > 2:
                farm.append(LittleCow(0))

    def countCow(farm,year):
        for i in range(year):
            j = len(farm)
            for k in range(j):
                lc = farm[k]
                lc.growUp(farm)

    farm = [LittleCow(1)]
    countCow(farm,year)
    return len(farm)


if __name__ == "__main__":
    for i in range(6):
        print(solution(i+1), end="; ")

    print()
    print("----------------------------")


    # F(n) = F(n-1) + F(n-3)

    def countCow2(year):
        if year==1 or year==2 or year==3:
            return year
        return countCow2(year-1) + countCow2(year-3)

    for i in range(6):
        print(countCow2(i+1), end="; ")


    print()
    print("----------------------------")

    # 非递归版
    def countCow3(year):
        a, b, c = 1, 2, 3
        for i in range(year-1):
            a, b, c = b, c, a + c
        return a

    for i in range(6):
        print(countCow3(i+1),end="; ")



