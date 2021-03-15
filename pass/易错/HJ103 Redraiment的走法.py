# coding=utf-8
"""
题目描述
   Redraiment是走梅花桩的高手。Redraiment总是起点不限，从前到后，往高的桩子走，但走的步数最多，不知道为什么？你能替Redraiment研究他最多走的步数吗？

样例输入
6
2 5 1 5 4 5

样例输出
3

提示
Example:
6个点的高度各为 2 5 1 5 4 5
如从第1格开始走,最多为3步, 2 4 5
从第2格开始走,最多只有1步,5
而从第3格开始走最多有3步,1 4 5
从第5格开始走最多有2步,4 5

所以这个结果是3。

接口说明
方法原型：
    int GetResult(int num, int[] pInput, List  pResult);
输入参数：
   int num：整数，表示数组元素的个数（保证有效）。
   int[] pInput: 数组，存放输入的数字。
输出参数：
   List pResult: 保证传入一个空的List，要求把结果放入第一个位置。
返回值：
  正确返回1，错误返回0

输入描述:
输入多行，先输入数组的个数，再输入相应个数的整数

输出描述:
输出结果

示例1
输入
复制
6
2
5
1
5
4
5
输出
复制
3
"""
# 闹了半天，就是个最长上升子序列的问题。
# 转化成求最长递增子序列
# 这种问题要使用动态规划方法来解，一种时间复杂度为O(n)2，另一种为nlog(n)。
# 提供一种nlog(n)的解法：
# 方法一
import bisect

while True:
    try:
        a, b = int(input()), map(int, input().split())
        q = []
        for v in b:
            pos = bisect.bisect_left(q, v)
            if pos == len(q):
                q.append(v)
            else:
                q[pos] = v
        print(len(q))
    except:
        break

# 方式二
# https://docs.python.org/zh-cn/3.6/library/bisect.html
import bisect

while True:
    try:
        a, b = int(input()), map(int, input().split())
        q = []
        for v in b:
            pos = bisect.bisect_left(q, v)
            if pos == len(q):
                q.append(v)
            else:
                q[pos] = v
        print(len(q))
    except:
        break


# 方法三
# 利用动态规划求解，整个问题可以转换为从前到后到第几个桩走的步数最多。
# 解析写在注释中(python版)：

def GetResult(l):
    n = len(l)  # 传入list的长度
    dp = [1] * n  # dp[i]表示以第i个桩为结尾，最多走多少步，初始是1步（默认这个桩是跟它之前相比最矮的）
    res = 0  # 整个问题的结果
    for i in range(n):  # i表示第几个桩
        for j in range(i):  # j表示i前面的桩
            if l[i] > l[j]:  # 如果第i个桩前面有比它矮的（比如是j），
                # 且以第j个桩为结尾走的步数是最多的，
                # 步数就是dp[j]+1，加的这个1表示从第j个走1步到第i个桩；另一种就是dp[i],默认等于1，但是
                # 遍历j的过程可能会更新这个值，因此取上述两个结果中最大的那个值，表示第i个桩为结尾，
                # 最多走多少步
                dp[i] = max(dp[i], dp[j] + 1)
        res = max(res, dp[i])  # 到第i个桩时最多走几步
    return res


while True:
    try:
        n = int(input())  # 几个点
        str_input = input().split()
        l = [int(v) for v in str_input]  # 输入的数组成的集合
        # l=[2,5,1,5,4,5]
        # print(l)
        ans = GetResult(l)
        print(ans)
    except:
        break
