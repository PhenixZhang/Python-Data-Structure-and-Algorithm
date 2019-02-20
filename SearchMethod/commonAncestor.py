# -- coding:utf-8 --


# The lowest common ancestor is defined between two nodes p and q
# as the lowest node in T that has both p and q as descendants
# where we allow a node to be a descendant of itself


#         3
#    1          5
# 0     2     4     8
#                 6
#                   7


from SearchMethod.BinarySearchTree import BSTnode


def lowestCommonAncestor(rt,p,q):
    while rt:
        if rt.data > p and rt.data > q:
            rt = rt.left
        elif rt.data < p and rt.data < q:
            rt = rt.right
        else:
            return rt


if __name__ == "__main__":
    alist = [3,1,5,0,8,2,6,4,7]
    bst = BSTnode(3)
    for each in alist:
        bst.insert(each)
    bst.show()

    print()
    result = lowestCommonAncestor(bst,6,1)
    if result:
        result.show()




