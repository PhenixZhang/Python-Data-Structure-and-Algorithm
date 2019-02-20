# 二叉树的 前中后遍历的非递归版  以及  可以拐弯的'层序遍历'


def preOrderTraverse(rt):
    lst = []
    if rt is None:
        return

    p = rt
    stack = []
    while p is not None:
        while p is not None:
            lst.append(p)
            if p.rchild is not None:
                stack.append(p.rchild)
            p = p.lchild

        if len(stack) > 0:
            p = stack.pop()
    return lst


def inOrderTraverse(rt):
    lst = []
    if rt is None:
        return

    p = rt
    stack = []
    while p is not None or len(stack)>0:
        while p is not None:
            stack.append(p)
            p = p.lchild

        if len(stack)>0:
            p = stack.pop()
            lst.append(p)
            p = p.rchild
    return lst


def postOrderTraverse(rt):
    lst = []
    if rt is None:
        return

    p = rt
    stack = []
    while p is not None or len(stack)>0:
        while p is not None:
            # 将根节点入栈
            stack.append(p)
            # 先左后右不断深入
            if p.lchild is not None:
                p = p.lchild
            else:
                p = p.rchild

        if len(stack)>0:
            p = stack.pop()
            lst.append(p)

        while len(stack)>0 and stack[-1].rchild is p:
            p = stack.pop()
            lst.append(p)

        if len(stack)>0:
            p = stack[-1].rchild
        else :
            p = None

    return lst




# 拐弯层序遍历

def turnAroundLevelSort(rt):
    lst = []
    if rt is None:
        return
    stack1 = []
    stack2 = []

    stack1.append(rt)

    while len(stack1)>0 or len(stack2)>0:
        while len(stack1)>0:
            p = stack1.pop()
            lst.append(p)
            if p.lchild is not None:
                stack2.append(p.lchild)
            if p.rchild is not None:
                stack2.append(p.rchild)

        while len(stack2)>0:
            p = stack2.pop()
            lst.append(p)
            if p.rchild is not None:
                stack1.append(p.rchild)
            if p.lchild is not None:
                stack1.append(p.lchild)
    return lst



if __name__ == "__main__":
    from BinaryTree import BinaryTree
    binary_tree = BinaryTree()
    for i in range(1, 9):
        binary_tree.insert(i)
    print(binary_tree.preorder(binary_tree.root))
    prelst = [each.data for each in preOrderTraverse(binary_tree.root)]
    print(prelst)

    print("-----------------------------")
    print(binary_tree.inorder(binary_tree.root))
    inlst = [each.data for each in inOrderTraverse(binary_tree.root)]
    print(inlst)


    print("-----------------------------")
    print(binary_tree.postorder(binary_tree.root))
    postlst = [each.data for each in postOrderTraverse(binary_tree.root)]
    print(postlst)


    print("-----------------------------")
    binary_tree.insert(9)
    binary_tree.traverse()
    turnAroundlst = [each.data for each in turnAroundLevelSort(binary_tree.root)]
    print(turnAroundlst)









