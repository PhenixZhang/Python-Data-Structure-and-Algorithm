# -- coding:utf-8 --


class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            tem = [self.root]
            while True:
                p = tem.pop(0)
                if p.lchild is None:
                    p.lchild = node
                    return
                if p.rchild is None:
                    p.rchild = node
                    return
                tem.append(p.lchild)
                tem.append(p.rchild)

    def traverse(self):
        if self.root is None:
            return None
        tem = [self.root]
        data_list = []
        while len(tem) > 0:
            cur = tem.pop(0)
            data_list.append(cur.data)
            if cur.lchild is not None:
                tem.append(cur.lchild)
            if cur.rchild is not None:
                tem.append(cur.rchild)
        print(data_list)

    def preorder(self, root):
        tem = []
        if root is None:
            return []
        tem.append(root.data)
        llist = self.preorder(root.lchild)
        rlist = self.preorder(root.rchild)
        return tem + llist + rlist

    def inorder(self, root):
        tem = []
        if root is None:
            return []
        llist = self.inorder(root.lchild)
        tem.append(root.data)
        rlist = self.inorder(root.rchild)
        return llist + tem + rlist

    def postorder(self, root):
        tem = []
        if root is None:
            return []
        llist = self.postorder(root.lchild)
        rlist = self.postorder(root.rchild)
        tem.append(root.data)
        return llist + rlist + tem

if __name__ == "__main__":
    binary_tree = BinaryTree()
    for i in range(1, 11):
        binary_tree.insert(i)
    print('------init binary_tree-----')
    binary_tree.traverse()
    print('------preorder result------')
    print(binary_tree.preorder(binary_tree.root))

    print('------inorder result------')
    print(binary_tree.inorder(binary_tree.root))

    print('------postorder result------')
    print(binary_tree.postorder(binary_tree.root))
