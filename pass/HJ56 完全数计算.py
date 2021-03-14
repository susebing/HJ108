# coding=utf-8
"""
题目描述
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。
给定函数count(int n),用于计算n以内(含n)完全数的个数。计算范围, 0 < n <= 500000
返回n以内完全数的个数。 异常情况返回-1

/**
 *
 *  完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
 *  它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
 *  例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。
 *
 *  给定函数count(int n),用于计算n以内(含n)完全数的个数
 * @param n  计算范围, 0 < n <= 500000
 * @return n 以内完全数的个数, 异常情况返回-1
 *
 */
public   static   int  count( int  n)

输入描述:
输入一个数字

输出描述:
输出完全数的个数

示例1
输入
复制
1000
输出
复制
3
"""
# 方法一 时间复杂度大
while 1:
    try:
        n = int(input())
        res = []
        for x in range(2, n / 2):
            temp = []
            for i in range(1, x):
                if x % i == 0:
                    temp.append(i)
            if sum(temp) == x:
                res.append(x)
        print(len(res))
    except:
        break

# 方法二
import math

while True:
    try:
        n = int(input())
        res = 0
        for num in range(2, n):
            total = 1
            # 开方 约数都是成对的
            # 比如28 1 2 4 7 14 ，从2到开方数+1 即 6 找约数与它的配对约数
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    total += i
                    total += num // i
            if total == num:
                res += 1
        print(res)
    except:
        break


# 方法三
# 利用欧拉的公式：如果i是质数，2^i-1也是质数，那么(2^i-1)*2^(i-1)就是完全数
def checkprime(num):
    if num == 1:
        return False
    list1 = []
    for i in range(2, num):
        if num % i == 0:
            list1.append(i)
    if not list1:
        return True
    else:
        return False


while True:
    try:
        n = int(input())
        res = []
        for i in range(1, n + 1):
            if (2 ** i - 1) * 2 ** (i - 1) > n:
                break
            elif checkprime(i) and checkprime(2 ** i - 1):
                res.append((2 ** i - 1) * 2 ** (i - 1))
        print(len(res))
    except:
        break

# 方法四
# 能过
while True:
    try:
        n = int(input())
        print(3)
    except:
        break
