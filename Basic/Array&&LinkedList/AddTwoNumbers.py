# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

from LinkedList import LinkedList, Node


def addTwoNums(ln1, ln2):
    ln1stack = buildStack(ln1)
    ln2stack = buildStack(ln2)

    head = Node()
    carry = 0
    while len(ln1stack)>0 or len(ln2stack)>0 or carry != 0:
        x = 0 if len(ln1stack)==0 else ln1stack.pop().data
        y = 0 if len(ln2stack) == 0 else ln2stack.pop().data
        sum = x + y + carry
        node = Node(sum % 10)
        node.next = head.next
        head.next = node
        carry = sum//10

    return head.next


def buildStack(ln):
    stack = []
    while ln is not None:
        stack.append(ln)
        ln = ln.next
    return stack


if __name__ == "__main__":
    linkedlist = LinkedList()
    for each in [7,2,4,3]:
        linkedlist.append(each)
    headA = linkedlist.getRoot()
    ln1 = headA.next

    linkedlist = LinkedList()
    for each in [5,6,4]:
        linkedlist.append(each)
    headB = linkedlist.getRoot()
    ln2 = headB.next

    p = addTwoNums(ln1,ln2)
    while p is not None:
        print(p.data, end="->")
        p = p.next