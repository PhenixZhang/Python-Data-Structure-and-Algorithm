# Given tree s:
#      3
#     / \
#    4   5
#   / \
#  1   2
#
# Given tree t:
#    4
#   / \
#  1   2
#
# Return true, because t has the same structure and node values with a subtree of s.
#
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
#
# Given tree t:
#    4
#   / \
#  1   2
#
# Return false.



def isSubTree(s, t):
    if s is None :
        return False
    return isSubTreeWithRoot(s, t) or isSubTree(s.lchild, t) or isSubTree(s.rchild, t)


def isSubTreeWithRoot(s, t):
    if s is None and t is None:
        return True
    if s is None or t is None:
        return False
    if s.data != t.data:
        return False
    return isSubTreeWithRoot(s.lchild,t.lchild) and isSubTreeWithRoot(s.rchild,t.rchild)




if __name__ == "__main__":
    from BinaryTree import BinaryTree
    binary_tree = BinaryTree()
    for i in range(1, 9):
        binary_tree.insert(i)
    binary_tree.traverse()
    s = binary_tree.root

    t = BinaryTree()
    for i in [2,4,5,8]:
        t.insert(i)
    t.traverse()
    t = t.root

    print(isSubTree(s, t))




