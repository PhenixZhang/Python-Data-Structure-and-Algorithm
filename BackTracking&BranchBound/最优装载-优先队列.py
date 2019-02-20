# -- coding:utf-8 --

from queue import PriorityQueue


def maxLoading(w, c):

    q = PriorityQueue()
    n = len(w)
    r = [0] * n
    for j in range(n-2,-1,-1):
        r[j] = r[j+1] + w[j+1]

    class Node():
        # data：存放货物重量
        # level：存放所在层数
        # isadded：用于记录该节点中level号下标的货物是否装载
        # par：指向父节点
        def __init__(self,data,level,isadded,par):
            self.data = data
            self.level = level
            self.isadded = isadded
            self.par = par

        # 为了降序排列
        def __gt__(self,other):
            return self.data < other.data

    def addLiveNode(wt, i, isadded,par):
            q.put(Node(wt,i,isadded,par))

    e = Node(0,-1,False,None)
    q.put(e)

    while True:
        e = q.get()
        i = e.level
        ew = e.data - r[i]
        if i == n-1:
            break
        # 每一层都要考虑是否要该层的那一个货物
        if ew + w[e.level+1] <= c:
            addLiveNode(ew + w[e.level+1] + r[e.level+1], e.level+1, True, e)
        addLiveNode(ew + r[e.level+1],e.level+1, False, e)

    return ew, e


if __name__ == "__main__":
    w = [5,40,15,30,20,50]
    c = 102
    ew, obj = maxLoading(w,c)
    print(ew)
    order = []
    while obj.par is not None:
        order.insert(0,obj.isadded)
        obj = obj.par
    print(order)











