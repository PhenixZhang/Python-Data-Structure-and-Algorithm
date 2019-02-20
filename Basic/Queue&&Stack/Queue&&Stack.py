# -- coding:utf-8 --

# 队列 先进先出 尾进头出
from queue import Queue

q = Queue()
q.put('a')
q.put('b')
q.put('c')

while not q.empty():
    print(q.get(),end=", ")

print()
print("----------------------")
print("----------------------")


# 优先队列

from queue import PriorityQueue

q = PriorityQueue()

q.put(5)
q.put(3)
q.put(9)

while not q.empty():
    print(q.get())


class OBJ():
    def __init__(self,data):
        self.data = data

    def __gt__(self, other):
        return self.data > other.data


o1 = OBJ(5)
o2 = OBJ(3)
o3 = OBJ(9)
o4 = OBJ(9)
o5 = OBJ(5)


print("-------------------")

q.put(o1)
q.put(o2)
q.put(o3)
q.put(o4)
q.put(o5)

while not q.empty():
    print(q.get().data)

print(o3,o4)




print("-------------------")
print("-------------------")


# 栈 后进先出
from Stack import Stack

s = Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

