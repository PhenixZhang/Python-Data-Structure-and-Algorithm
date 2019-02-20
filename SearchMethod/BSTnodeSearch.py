# -- coding:utf-8 --
from SearchMethod.BinarySearchTree import BSTnode


def BSTnodeSearch(rt,target):
    if not rt:
        return None
    if rt.data == target:
        return rt
    elif rt.data > target :
        return BSTnodeSearch(rt.left,target)
    else :
        return BSTnodeSearch(rt.right,target)



# find min
def searchMinNode(rt):
    if rt:
        while rt.left:
            rt = rt.left
    return rt


# find max
def searchMaxNode(rt):
    if rt:
        while rt.right:
            rt = rt.right
    return rt


if __name__ == "__main__":
    alist = [4,3,6,7,8,9,3,2,5,7]
    bst = BSTnode(6)
    for each in alist:
        bst.insert(each)
    bst.show()
    print()
    result = BSTnodeSearch(bst,4)
    if result:
        result.show()
    print()
    print("max: %s" % searchMaxNode(bst).data)
    print("min: %s" % searchMinNode(bst).data)



