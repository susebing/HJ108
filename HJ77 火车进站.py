# coding=utf-8
"""
题目描述
给定一个正整数N代表火车数量，0<N<10，接下来输入火车入站的序列，一共N辆火车，每辆火车以数字1-9编号，火车站只有一个方向进出，同时停靠在火车站的列车中，只有后进站的出站了，先进站的才能出站。要求以字典序排序输出火车出站的序列号。

输入描述:
有多组测试用例，每一组第一行输入一个正整数N（0<N<10），第二行包括N个正整数，范围为1到9。

输出描述:
输出以字典序从小到大排序的火车出站序列号，每个编号以空格隔开，每个输出序列换行，具体见sample。

示例1
输入
复制
3
1 2 3
输出
复制
1 2 3
1 3 2
2 1 3
2 3 1
3 2 1
"""


def in_out(index, train, station, out, res):
    if train[-1] in station:  # 火车全部进站，只能出站
        res.append(" ".join(out + station[::-1]))
        return
    if station == []:  # 车站无火车，只能进站
        in_out(index + 1, train, station + [train[index]], out, res)
    else:
        in_out(index, train, station[:-1], out + [station[-1]], res)  # 出站
        in_out(index + 1, train, station + [train[index]], out, res)  # 进站


while True:
    try:
        n = int(input())
        order = input().split()
        res = []
        in_out(0, order, [], [], res)
        res.sort()
        print('\n'.join(res))
    except:
        break
