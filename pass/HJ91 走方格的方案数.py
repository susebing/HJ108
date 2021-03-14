# coding=utf-8
"""
题目描述
请编写一个函数（允许增加子函数），计算n x m的棋盘格子（n为横向的格子数，m为竖向的格子数）沿着各自边缘线从左上角走到右下角，总共有多少种走法，要求不能走回头路，即：只能往右和往下走，不能往左和往上走。
输入描述:
输入两个正整数

输出描述:
返回结果

示例1
输入
复制
2
2
输出
复制
6
"""


# 用递归来做，将右下角看做原点(0, 0)，左上角看做坐标(m, n)，下图所示：
# 从(m, n)—>(0, 0)就分两步走：
# 往右走一步：f(m, n - 1)—>(0, 0) 加上下走一步：f(m - 1, n)—>(0, 0)

# 注意：但凡是触碰到边界，也就是说f(x, 0)或者f(0,x)都只有一条直路可走了，这里的x是变量哈。
# f(m, n) = f(m, n - 1) + f(m - 1, n)
# 按照这种思想，算法就很简单了，代码如下

def f(n, m):
    if n == 0 or m == 0:
        return 1
    else:
        return f(n - 1, m) + f(n, m - 1)


while True:
    try:
        n, m = map(int, input().split())
        print(f(n, m))
    except:
        break


# 方法二
# 我来分享一下我的python解法，使用动态规划。
# 草草看了下其他人的解法，都是使用递归，这样对于大的m和n，肯定时间复杂度是不满足的，
# 这道题的测试用例还是太easy。
# 这道题在代码里面下了毒，明明输入是一行，题目非要说是两行，对我的心理造成了极大的创伤。
# 输入部分使用了解包，与lambda函数结合，食用更佳。
def uniquePath(m, n):
    if m == 1 or n == 1:
        return 1
    result = [[0 for i in range(n)]] * m
    for i in range(m):
        result[i][0] = 1
    for i in range(n):
        result[0][i] = 1
    for i in range(1, m):
        for j in range(1, n):
            result[i][j] = result[i - 1][j] + result[i][j - 1]
    return result[m - 1][n - 1]


while True:
    try:
        print(uniquePath(*map(lambda c: int(c) + 1, input().split())))
    except:
        break
