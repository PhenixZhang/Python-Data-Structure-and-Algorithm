# -- coding:utf-8 --


# [[1,1,0,1],
#  [1,0,1,0],
#  [1,1,1,1],
#  [1,0,1,1]]

# 1 表示可以经过某个位置，求解从 (0, 0) 位置到 (tr, tc) 位置的最短路径长度。

from queue import Queue

def minPathLength(graph,tr,tc):
    direction = ((1,0),(-1,0),(0,1),(0,-1))
    m = len(graph)
    n = len(graph[0])
    q = Queue()
    q.put((0,0))
    pathLength = 0
    while not q.empty():
        size = q.qsize()
        pathLength += 1
        while size > 0:
            size -= 1
            cr, cc = q.get()
            graph[cr][cc] = 0
            for d in direction:
                nr = cr + d[0]
                nc = cc + d[1]
                if nr<0 or nr>=m or nc<0 or nc>=n or graph[nr][nc]==0:
                    continue
                if nr == tr and nc == tc:
                    return pathLength
                q.put((nr,nc))
    return -1




if __name__ == "__main__":
    graph = [[1, 1, 0, 1],
             [1, 0, 1, 0],
             [1, 1, 1, 1],
             [1, 0, 1, 1]]

    print(minPathLength(graph,1,2))