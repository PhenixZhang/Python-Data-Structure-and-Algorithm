# Input:
#
#          1
#         / \
#        2  3
#       / \
#      4   5
#
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# 如何求一颗树的深度



def depth(rt):
    if rt is None:
        return 0
    leftdepth = depth(rt.lchild)
    rightdepth = depth(rt.rchild)
    return max(leftdepth, rightdepth) + 1


def diameterOfBinaryT(rt):
    maxD = 0
    ld = depth(rt.lchild)
    lr = depth(rt.rchild)
    maxD = max(maxD, ld + lr)
    return maxD


if __name__ == "__main__":
    from BinaryTree import BinaryTree

    binary_tree = BinaryTree()
    for i in range(1, 5):
        binary_tree.insert(i)
    binary_tree.traverse()

    print(diameterOfBinaryT(binary_tree.root))