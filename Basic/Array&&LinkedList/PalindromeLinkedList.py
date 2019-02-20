# 回文链表
from LinkedList import LinkedList, Node


def isPalindrome(head):
    if head is None or head.next is None:
        return True

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    if fast is not None:
        slow = slow.next

    cut(head, slow)
    return isEqual(head, reverse(slow))


def cut(head, cutNode):
    while head.next is not cutNode:
        head = head.next
    head.next = None


def reverse(head):
    newHead = None
    while head is not None:
        nextNode = head.next
        head.next = newHead
        newHead = head
        head = nextNode
    return newHead


def isEqual(ln1, ln2):
    while ln1 is not None and ln2 is not None:
        if ln1.data != ln2.data:
            return False
        ln1 = ln1.next
        ln2 = ln2.next

    return True




if __name__ == "__main__":
    linkedlist = LinkedList()
    for each in "abcdedcba":
        linkedlist.append(each)
    head = linkedlist.getRoot().next

    print(isPalindrome(head))


    linkedlist = LinkedList()
    for each in "abcddcba":
        linkedlist.append(each)
    head = linkedlist.getRoot().next

    print(isPalindrome(head))

    linkedlist = LinkedList()
    for each in "axcddcba":
        linkedlist.append(each)
    head = linkedlist.getRoot().next

    print(isPalindrome(head))





