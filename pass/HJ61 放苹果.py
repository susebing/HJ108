# coding=utf-8
"""
题目描述
题目描述
把M个同样的苹果放在N个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？（用K表示）5，1，1和1，5，1 是同一种分法。
输入
每个用例包含二个整数M和N。0<=m<=10，1<=n<=10。
样例输入
7 3
样例输出
8
/**
* 计算放苹果方法数目
* 输入值非法时返回-1
* 1 <= m,n <= 10
* @param m 苹果数目
* @param n 盘子数目数
* @return 放置方法总数
*
*/
public static int count(int m, int n)

输入描述:
输入两个int整数

输出描述:
输出结果，int型

示例1
输入
复制
7 3
输出
复制
8
"""


# 把M个同样的苹果放在N个同样的盘子里，
# 允许有的盘子空着不放，问共有多少种不同的分法？
# （用K表示）5，1，1和1，5，1 是同一种分法。
def put(m, n):
    # put(m,n-1)有空盘子的分法数（递归）
    # put(m-n,n)无空盘子的分法数
    if (n == 1) or (m < 1):
        return 1
    if m < n:
        return put(m, m)
    else:
        return (put(m, n - 1) + put(m - n, n))


while 1:
    try:
        m, n = map(int, input().split())
        print(put(m, n))
    except:
        break
