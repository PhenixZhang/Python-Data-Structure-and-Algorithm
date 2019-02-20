import queue

'''
二叉树结点
'''


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def settag(self, tag=None):
        self.tag = tag


def visit(treenode):
    print(str(treenode.val), end=' ')


'''
根据前序中序遍历非递归构造二叉树
'''


def ConstructTreeByPreInOrder(preorder, inorder):
    print('ConstructTreeByPreInOrder:', end=' ')
    treesize = len(preorder)
    root = TreeNode(preorder[0])
    isvisited = []
    for i in range(treesize):
        isvisited.append(0)
    stactnode = queue.LifoQueue()   # 栈
    rootindex = inorder.index(preorder[0])
    isvisited[rootindex] = 1
    cur = root
    j = 1
    while (j < treesize):
        if (rootindex > 0 and isvisited[rootindex - 1] != 1):  # 构造左子树
            cur.left = TreeNode(preorder[j])
            rootindex = inorder.index(preorder[j])
            isvisited[rootindex] = 1
            j += 1
            stactnode.put(cur)
            cur = cur.left
        elif (rootindex < treesize and isvisited[rootindex + 1] != 1):  # 构造右子树
            cur.right = TreeNode(preorder[j])
            rootindex = inorder.index(preorder[j])
            j += 1
            isvisited[rootindex] = 1
            cur = cur.right
        else:
            cur = stactnode.get()
            rootindex = inorder.index(cur.val)
    PostOrder(root)  # 后序遍历输出构造的二叉树


def PostOrder(root):
    if root is None:
        return

    PostOrder(root.left)
    PostOrder(root.right)
    print(root.val, end=" ")




if __name__=='__main__':
    preorder = [1, 2, 4, 3, 5, 6, 7]
    inorder = [2, 4, 1, 5, 3, 7, 6]
    postorder = [4, 2, 5, 7, 6, 3, 1]
    ConstructTreeByPreInOrder(preorder, inorder)
