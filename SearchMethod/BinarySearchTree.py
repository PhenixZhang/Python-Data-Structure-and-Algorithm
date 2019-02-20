# -- coding:utf-8 --
from queue import Queue


class BSTnode():
    # data：数据域  left：指向左子树  right：指向右子树
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self,x):
        # 若数据等于当前节点值，不进行任何操作
        # 如果数据小于当前节点值，则在左子树中找寻合适的位置
        if x < self.data:
            if self.left:
                self.left.insert(x)
            else:
                tree = BSTnode(x)
                self.left = tree
        # 如果数据大于当前节点值，则在右子树中找寻合适的位置
        elif x > self.data:
            if self.right:
                self.right.insert(x)
            else:
                tree = BSTnode(x)
                self.right = tree

    def show(self):
        # 使用队列层序遍历，展示结果
        q = Queue()
        q.put(self)
        while not q.empty():
            temp = q.get()
            print(temp.data,end="; ")
            if temp.left:
                q.put(temp.left)
            else :
                if temp.data != "None":
                    q.put(BSTnode("None"))
            if temp.right:
                q.put(temp.right)
            else :
                if temp.data != "None":
                    q.put(BSTnode("None"))


if __name__ == "__main__":
    alist = [4,3,6,7,8,9,3,2,5,7]
    bst = BSTnode(6)
    for each in alist:
        bst.insert(each)
    bst.show()




