# -- coding:utf-8 --

from LinkedList import LinkedList


def countBackwardsK(rt,k):
    p = rt
    pk = rt
    count = 0
    while p.getNext() is not None:
        p = p.getNext()
        if count > k-2:
            pk = pk.getNext()
        count += 1
    return pk


if __name__ == "__main__":
    linkedlist = LinkedList()
    for each in "abcdefghijklmnopqrst":
        linkedlist.append(each)
    print(len(linkedlist))
    print(linkedlist)
    rt = linkedlist.getRoot()
    ele = countBackwardsK(rt,5)
    print(ele)









