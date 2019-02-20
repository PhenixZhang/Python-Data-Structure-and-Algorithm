# -- coding:utf-8 --
# 依次按列放置皇后


def Queen(N):

    queen = [0] * N
    number = 0

    def attack(row, col):
        i = 0
        atk = False

        while not atk and i < col:
            offset_col = abs(i - col)
            offset_row = abs(queen[i] - row)
            if queen[i] == row or offset_col == offset_row:
                atk = True
            i += 1

        return atk

    def print_table():
        nonlocal number
        number += 1
        print("--------------------------")
        print("%d皇后问题的第%s组解" %(N,number))
        for x in range(N):
            for y in range(N):
                if x == queen[y]:
                    print("[*]",end="")
                else :
                    print("[ ]",end="")
            print()

    def decide_position(value):
        # i表示皇后的行号，因为按列依次放置皇后，那么对每一个皇后而言，列是固定的，需要扫描行号，value是列号
        i = 0
        while i < N:
            if not attack(i, value):
                queen[value] = i
                if value == N-1:
                    print_table()
                else:
                    decide_position(value+1)
            i += 1

    decide_position(0)


if __name__ == "__main__":
    Queen(8)






