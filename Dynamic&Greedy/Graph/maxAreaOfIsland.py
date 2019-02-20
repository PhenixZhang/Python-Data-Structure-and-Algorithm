# -- coding:utf-8 --


def maxAreaOfIsland(graph):
    m = len(graph)
    n = len(graph[0])
    maxArea = 0

    for i in range(m):
        for j in range(n):
            maxArea = max(maxArea,dfs(graph,i,j))
    return maxArea


def dfs(graph,r,c):
    m = len(graph)
    n = len(graph[0])
    direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
    if r<0 or r>=m or c<0 or c>=n or graph[r][c]==0:
        return 0

    graph[r][c] = 0
    area = 1
    for d in direction:
        area += dfs(graph,r+d[0],c+d[1])
    return area



if __name__ == "__main__":
    graph = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    print(maxAreaOfIsland(graph))





