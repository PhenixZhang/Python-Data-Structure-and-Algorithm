

def findPostorder(preorder,low1,high1, inorder,low2,high2, postorder,low3,high3):
    if low1 > high1:
        return
    if low1 == high1:
        postorder[high3] = preorder[low1]
        return

    i = 0
    for i in range(high2 -low2 + 1):
        if preorder[low1] == inorder[i+low2]:
            break

    postorder[high3] = preorder[low1]
    findPostorder(preorder,low1+1,low1+i, inorder,low2,low2+i-1, postorder,low3,low3+i-1)
    findPostorder(preorder,low1+i+1,high1, inorder,low2+i+1,high2, postorder,low3+i,high3-1)


if __name__ == "__main__":

    pre=[1,2,4,7,3,5,6,8]
    tin=[4,7,2,1,5,3,8,6]
    n = len(pre)
    postorder = [0] * n
    findPostorder(pre,0,n-1, tin,0,n-1, postorder,0,n-1)
    print(postorder)