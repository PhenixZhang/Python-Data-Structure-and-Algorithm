class LinearSet(object):

    def __init__(self):
        self.items = []

    def add(self, k):
        for each in self.items:
            if each == k:
                return
        self.items.append(k)

    def has(self, k):
        for key in self.items:
            if key == k:
                return True
        return False


class BetterSet(object):

    def __init__(self, n=100):
        self.maps = []
        for i in range(n):
            self.maps.append(LinearSet())

    def find_map(self, k):
        index = hash(k) % len(self.maps)
        return self.maps[index]

    def add(self, k):
        m = self.find_map(k)
        m.add(k)

    def has(self, k):
        m = self.find_map(k)
        return m.has(k)


class HashMap(object):
    def __init__(self):
        self.maps = BetterSet(2)
        self.num = 0

    def has(self, k):
        return self.maps.has(k)

    def add(self, k):
        if self.num == len(self.maps.maps):
            self.resize()

        self.maps.add(k)
        self.num += 1

    def resize(self):
        new_map = BetterSet(self.num * 2)

        for m in self.maps.maps:
            for k in m.items:
                new_map.add(k)

        self.maps = new_map


if __name__ == '__main__':
    import time
    m = HashMap()
    s = ['a','b','c',1,2]
    for k in s:
        m.add(k)

    for k in ['c','a','d','b',4,1,2,5]:
        print(k, m.has(k))
        time.sleep(1)
