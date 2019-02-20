# -- coding:utf-8 --

class Stack:
    # 用列表模拟栈，列表头为栈的底部，列表末尾为栈的顶部
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    # 从末尾放入
    def push(self, item):
        self.items.append(item)

    # 从末尾取出
    def pop(self):
        return self.items.pop()

    # 查看最末尾的数
    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)










