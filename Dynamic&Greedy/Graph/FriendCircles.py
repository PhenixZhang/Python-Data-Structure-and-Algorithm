# -- coding:utf-8 --


# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
#
# Output: 2
#
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
# The 2nd student himself is in a friend circle. So return 2.


def findCircleNum(graph):
    m = len(graph)
    circleNum = 0
    hasVisited = [0] * m
    for i in range(m):
        if not hasVisited[i]:
            dfs(graph,i,hasVisited)
            circleNum += 1

    return circleNum


def dfs(graph,i,hasVisited):
    m = len(graph)
    hasVisited[i] = 1
    for k in range(m):
        if graph[i][k] == 1 and not hasVisited[k]:
            dfs(graph,k,hasVisited)


if __name__ == "__main__":
    graph = [[1,1,0],
             [1,1,0],
             [0,0,1]]
    print(findCircleNum(graph))


