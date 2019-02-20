# -- coding:utf-8 --


def sequentialSearch(lst,target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i

    return -1


if __name__ == "__main__":
    alist = [4,3,6,7,8,9,3,2,54,7]
    print(sequentialSearch(alist,53))









