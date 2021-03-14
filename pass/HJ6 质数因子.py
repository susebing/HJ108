"""
题目描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）

最后一个数后面也要有空格

输入描述:
输入一个long型整数

输出描述:
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。

示例1
输入
复制
180
输出
复制
2 2 3 3 5
"""

# 为啥不判断是不是质因子：因为从2开始除这个数，2如果能除尽，
# 就用2除（换言之就轮不到4，8，10等来除）；
# 2不能除，那用3去除，3能除尽就除，除不尽i继续递增；

# 假如i递增到4了（同志们想想是不是直接将4pass了？
# 因为4如果能除尽，那么它前面的2就已经去除了，根本轮不到4除），

# i再增到5，能除尽就除，除不尽用下一个6去除，同理，肯定pass，
# 因为6如果能除尽，前面的3早就除了，轮不到6去除。。。
# 由此可知，得到的因子自然就是质因子了
#
# 需要注意的是输出的最后一个质数因子也需要以空格结束

while 1:
    try:
        n = 2
        a = int(input())
        while a >= n * n:
            if a % n == 0:
                print(n, end=' ')
                a //= n
            else:
                n += 1
        print(a, end=' ')
    except:
        break