# coding=utf-8
"""
题目描述
问题描述：数独（Sudoku）是一款大众喜爱的数字逻辑游戏。玩家需要根据9X9盘面上的已知数字，推算出所有剩余空格的数字，并且满足每一行、每一列、每一个粗线宫内的数字均含1-9，并且不重复。
输入：
包含已知数字的9X9盘面数组[空缺位以数字0表示]
输出：
完整的9X9盘面数组

输入描述:
包含已知数字的9X9盘面数组[空缺位以数字0表示]

输出描述:
完整的9X9盘面数组

示例1
输入
复制
0 9 2 4 8 1 7 6 3
4 1 3 7 6 2 9 8 5
8 6 7 3 5 9 4 1 2
6 2 4 1 9 5 3 7 8
7 5 9 8 4 3 1 2 6
1 3 8 6 2 7 5 9 4
2 7 1 5 3 8 6 4 9
3 8 6 9 1 4 2 5 7
0 4 5 2 7 6 8 3 1
输出
复制
5 9 2 4 8 1 7 6 3
4 1 3 7 6 2 9 8 5
8 6 7 3 5 9 4 1 2
6 2 4 1 9 5 3 7 8
7 5 9 8 4 3 1 2 6
1 3 8 6 2 7 5 9 4
2 7 1 5 3 8 6 4 9
3 8 6 9 1 4 2 5 7
9 4 5 2 7 6 8 3 1
"""


def cal(result, p):
    x, y = p
    if x > 8: return True
    nextp = (x, y + 1)
    if y >= 8:
        nextp = (x + 1, 0)
    m = []
    if result[x][y] != 0:
        return cal(result, nextp)
    for i in range(int(x / 3) * 3, int(x / 3) * 3 + 3):
        m += result[i][int(y / 3) * 3:int(y / 3) * 3 + 3]
    for i in range(1, 10):
        if not (i in result[x] or i in [k[y] for k in result] or i in m):
            result[x][y] = i
            if cal(result, nextp):
                return True
    else:
        result[x][y] = 0
        return False


inlist = []
for i in range(9):
    inlist.append([int(x) for x in input().split()])
cal(inlist, (0, 0))
for l in inlist:
    print(' '.join([str(s) for s in l]))
