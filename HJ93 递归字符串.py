# coding=utf-8
"""
题目描述
编写一个函数，传入一个int型数组，返回该数组能否分成两组，使得两组中各元素加起来的和相等，并且，所有5的倍数必须在其中一个组中，所有3的倍数在另一个组中（不包括5的倍数），能满足以上条件，返回true；不满足时返回false。
输入描述:
第一行是数据个数，第二行是输入的数据

输出描述:
返回true或者false

示例1
输入
复制
4
1 5 -5 1
输出
复制
true
"""
# 本题相对来说比较简单，使用深度优先搜素算法即可。
# 对输入的数进行分组：
# 5的倍数一组 arr5,
# 3的倍数一组 arr3，
# 剩余的数一组 arr。
# 这三组数的和需要满足如下关系：

while True:
    try:
        n = int(input())
        a = list(map(int, input().split()))
        arr5 = []
        arr3 = []
        arr = []
        for i in a:
            if i % 5 == 0:
                arr5.append(i)
            elif i % 3 == 0:
                arr3.append(i)
            else:
                arr.append(abs(i))

        sum_arr5 = sum(arr5)
        sum_arr3 = sum(arr3)
        sum_arr = sorted(arr, reverse=True)

        for i in sum_arr:
            if sum_arr5 < sum_arr3:
                sum_arr5 += i
            else:
                sum_arr3 += i
        print('true' if sum_arr5 == sum_arr3 else 'false')

    except:
        break
