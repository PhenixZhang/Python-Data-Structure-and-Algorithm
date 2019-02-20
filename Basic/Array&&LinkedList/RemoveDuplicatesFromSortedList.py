# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

from LinkedList import LinkedList, Node


def deleteDuplicates(head):
    if head is None or head.next is None:
        return head
    head.next = deleteDuplicates(head.next)
    return head.next if head.data == head.next.data else head



if __name__ == "__main__":
    linkedlist = LinkedList()
    for each in [1,1,2,3,3]:
        linkedlist.append(each)
    headA = linkedlist.getRoot()
    ln = headA.next
    tmp = ln
    while tmp is not None:
        print(tmp.data, end="->")
        tmp = tmp.next

    print()
    p = deleteDuplicates(ln)
    while p is not None:
        print(p.data, end="->")
        p = p.next