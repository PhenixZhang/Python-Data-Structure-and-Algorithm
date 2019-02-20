# -- coding:utf-8 --

class Node():
    # data：数据域  next：指向下一个节点的指针
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    __repr__ = __str__


    def getValue(self):
        return self.data

    def getNext(self):
        return self.next

    def setValue(self,newValue):
        self.data = newValue

    def setNext(self,newNext):
        self.next = newNext




class LinkedList():
    def __init__(self):
        self._head = Node()
        self._length = 0

    def __len__(self):
        return self._length

    def __str__(self):
        current = self._head.getNext()
        s = ''
        while current != None:
            s += str(current.getValue())+', '
            current = current.getNext()
        if s:
            s = s[:-2]
        s = '['+s+']'
        return s


    def isEmpty(self):
        return self._length == 0

    # 定义从头插入的方法
    def add(self,value):
        newNode = Node(value,None)
        newNode.setNext(self._head.next)
        self._head.next = newNode
        self._length += 1

    # 定义从末尾插入的方法
    def append(self,value):
        newNode = Node(value,None)
        current = self._head
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(newNode)
        self._length += 1

    # 定义根据索引插入的方法
    def insert(self,ind,value):
        if ind == 0:
            self.add(value)
        if ind < 0 or ind >= self._length:
            raise ValueError("index out of range...")

        newNode = Node(value,None)
        pre = self._head
        for i in range(ind):
            pre = pre.getNext()
        newNode.setNext(pre.getNext())
        pre.setNext(newNode)
        self._length += 1

    # 定义判断一个元素是否在链表中的方法
    def isIn(self,value):
        current = self._head.getNext()
        foundvalue = False
        while current != None and not foundvalue:
            if current.getValue() == value:
                foundvalue = True
            else :
                current = current.getNext()
        return foundvalue

    # 定义查找某个元素的索引的方法
    def indexOf(self,value):
        current = self._head.getNext()
        count = 0
        found = None
        while current != None and not found:
            if current.getValue() == value:
                found = True
            else:
                current = current.getNext()
                count += 1
        if found:
            return count
        else:
            raise ValueError('%s is not in linkedlist' %value)

    # 定义根据值删除链表中元素的方法
    def remove(self,value):
        if self.isEmpty():
            raise ValueError("linkedlist is already empty...")
        current = self._head.getNext()
        pre = self._head
        count = 0
        while current != None:
            if current.getValue() == value:
                pre.setNext(current.getNext())
                self._length -= 1
                break
            else:
                count += 1
                pre = current
                current = current.getNext()
        if count < self._length:
            print("%s has been removed." %value)
        else :
            print("%s not in linkedlist..." %value)

    # 定义根据索引删除链表中元素的方法
    def pop(self,ind):
        if ind >= self._length:
            raise ValueError("index out of range...")
        pre = self._head
        for i in range(ind):
            pre = pre.getNext()
        pre.setNext(pre.getNext().getNext())
        self._length -= 1


    # 为了后续操作，这里设置根节点接口
    def getRoot(self):
        return self._head


if __name__ == "__main__":
    linkedlist = LinkedList()
    print(len(linkedlist))
    print(linkedlist)
    linkedlist.add(5)
    linkedlist.add(6)
    linkedlist.append("a")
    linkedlist.append("b")
    print(len(linkedlist))
    print(linkedlist)
    linkedlist.insert(3,"m")
    print(len(linkedlist))
    print(linkedlist)
    linkedlist.pop(2)
    print(len(linkedlist))
    print(linkedlist)
    linkedlist.remove(5)
    print(len(linkedlist))
    print(linkedlist)


