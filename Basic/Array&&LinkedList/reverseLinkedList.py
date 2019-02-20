# -- coding:utf-8 --
from LinkedList import LinkedList, Node


def revLinkedList(rt):
    if rt.getNext() is None:
        raise ValueError("empty linkedlist...")
    newRt = None
    rt = rt.getNext()
    while rt != None:
        temp = rt.getNext()
        # 断开头节点与后面的链接
        rt.setNext(newRt)
        # 更新新的头节点
        newRt = rt
        # 更新旧的头节点
        rt = temp
    # 补充一个空的头节点
    newNode = Node()
    newNode.setNext(newRt)
    newRt = newNode
    return newRt


if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.add(5)
    linkedlist.add(6)
    linkedlist.append("a")
    linkedlist.append("b")
    linkedlist.insert(3,"m")
    print(len(linkedlist))
    print(linkedlist)

    rt = linkedlist.getRoot()
    nrt = revLinkedList(rt)
    nrt = nrt.getNext()
    while nrt is not None:
        print(nrt.getValue(),end=", ")
        nrt = nrt.getNext()


