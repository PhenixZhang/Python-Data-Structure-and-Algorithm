# 回溯

import random
#冲突检查函数
def conflict(state,nextX):
    '''
    state用来存储皇后摆放位置(tuple)
    nextX为下一个皇后的水平位置
    nextY为下一个皇后的垂直位置
    '''
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0,nextY - i):
            return True # #若下一个皇后和前面的皇后列相同或者在一条对角线上，则冲突
    return False

def queens(num,state=()):
    '''
    num表示规模
    '''
    for pos in range(num):
        if not conflict(state,pos): # 位置不冲突
            if len(state) == num - 1:   # 若是最后一个皇后，则返回该位置
                yield(pos, )
            else:     #若不是最后一个皇后,则将该位置返回到state元组并传给后面的皇后
                for result in queens(num,state + (pos, )): 
                    yield(pos, ) + result

# 可视化输出
def prettyprint(solution):
    def line(pos,length = len(solution)):
        return '.' * (pos) + 'X' + '.' * (length - pos -1)
    for pos in solution:
        print(line(pos))
    for item in queens(len(solution)):
        print(item)

if __name__ == '__main__':
    prettyprint(random.choice(list(queens(4))))
    # print(list(queens(4)))