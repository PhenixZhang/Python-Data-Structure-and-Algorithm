# -- coding:utf-8 --
from LinkedList import LinkedList


def findCircle(rt):
    if rt.getNext() is None :
        raise ValueError("empty linkedlist...")
    if rt.getNext().getNext() is None:
        raise ValueError("only one element in linkedlist...")
    p1 = rt.getNext()
    p2 = rt.getNext().getNext()
    while p1 is not p2 :
        if p2 is None:
            print("linkedlist has no circle...")
            return
        p1 = p1.getNext()
        temp = p2.getNext()
        if temp is None:
            print("linkedlist has no circle...")
            return
        p2 = temp.getNext()

    p2 = rt
    while p1 is not p2:
        p1 = p1.getNext()
        p2 = p2.getNext()

    return p1


if __name__ == "__main__":
    linkedlist = LinkedList()
    for each in "abcdefghijklmnopqrst":
        linkedlist.append(each)
    print(len(linkedlist))
    print(linkedlist)
    rt = linkedlist.getRoot()

    p1 = findCircle(rt)
    print(p1)
    print("-----------------------------")
    p = rt
    for i in range(15):
        p = p.getNext()
    print(p.getValue())
    q = rt
    while q.getNext() is not None:
        q = q.getNext()
    print(q.getValue())
    q.setNext(p)

    print("-----------------------------")
    p1 = findCircle(rt)
    print(p1)