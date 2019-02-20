# 分支限界
# 最优装载问题

# https://blog.csdn.net/lican19911221/article/details/26489305

from queue import Queue
def maxLoading(w, c):
    '''w:单个重量;c:最大装载重量;return:最好节点'''
    q = Queue() # 队列
    n = len(w)
    class Node():
        '''data：存放货物重量;level：存放所在层数;par：指向父节点
        isadded：用于记录该节点中，level号下标的货物是否装载'''
        def __init__(self,data,level,isadded,par):
            self.data = data
            self.level = level
            self.isadded = isadded
            self.par = par

    bestNode = Node(0,-1,False,None)    # 初始化
    # 定义增加节点函数
    def addLiveNode(wt, i, isadded,par):
        nonlocal bestNode, q
        # 如果到达了最末层
        if i == n-1:
            if wt > bestNode.data:
                bestNode = Node(wt,i,isadded,par)
        else :
            q.put(Node(wt,i,isadded,par))
    ew = Node(0,-1,False,None)
    q.put(ew)
    while not q.empty():
        ew = q.get()
        # 每一层都要考虑是否要该层的那一个货物
        if ew.data + w[ew.level+1] <= c:
            addLiveNode(ew.data + w[ew.level+1], ew.level+1, True, ew)
        addLiveNode(ew.data,ew.level+1, False, ew)
    return bestNode

if __name__ == "__main__":
    w = [5,40,15,30,20,50]
    c = 102
    obj = maxLoading(w,c)
    print(obj.data)
    order = []
    while obj.par is not None:
        order.insert(0,obj.isadded)
        obj = obj.par
    print(order)