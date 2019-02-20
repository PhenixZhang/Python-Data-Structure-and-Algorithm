# A:          a1 → a2
#                     ↘
#                       c1 → c2 → c3
#                     ↗
# B:    b1 → b2 → b3

from LinkedList import LinkedList, Node


def getIntersectionNode(headA, headB):
    p1 = headA
    p2 = headB
    while p1 is not p2:
        p1 = headB if p1 is None else p1.next
        p2 = headA if p2 is None else p2.next

    return p1



if __name__ == "__main__":
    linkedlist = LinkedList()
    for each in "abcdefghijklmn":
        linkedlist.append(each)
    headA = linkedlist.getRoot()
    tmp = headA
    while tmp.data != 'i':
        tmp = tmp.next
    headB = Node()
    headB.next = Node('x',Node('y',Node('z',tmp)))

    p = getIntersectionNode(headA,headB)
    print(p)
