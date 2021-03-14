# coding=utf-8
"""
题目描述
如果A是个x行y列的矩阵，B是个y行z列的矩阵，把A和B相乘，其结果将是另一个x行z列的矩阵C。这个矩阵的每个元素是由下面的公式决定的

输入描述:
输入包含多组数据，每组数据包含：
第一行包含一个正整数x，代表第一个矩阵的行数
第二行包含一个正整数y，代表第一个矩阵的列数和第二个矩阵的行数
第三行包含一个正整数z，代表第二个矩阵的列数
之后x行，每行y个整数，代表第一个矩阵的值
之后y行，每行z个整数，代表第二个矩阵的值

输出描述:
对于每组输入数据，输出x行，每行z个整数，代表两个矩阵相乘的结果
示例1
输入
复制
2
3
2
1 2 3
3 2 1
1 2
2 1
3 3
输出
复制
14 13
10 11
"""

# 假设两个矩阵，A是3*4的，B是4*5的，结果是3*5的
# A=[[1,2, 3, 4],
#   [5,6, 7, 8],
#   [9,10,11,12]]
# B=[[1,2,3,4,5],
#   [4,5,6,7,8],
#   [7,8,9,10,11],
#   [10,11,12,13,14]]
# 方法一
while True:
    try:
        x = int(input())  # 第一个矩阵的行数#3
        y = int(input())  # 第一个矩阵的列数和第二个矩阵的行数#4
        z = int(input())  # 第二个矩阵的列数#5
        A = []  # 矩阵A初始化
        B = []  # 矩阵B初始化
        for i in range(x):  # 矩阵A赋值
            li = input().split()
            li = [int(v) for v in li]
            A.append(li)
        for j in range(y):  # 矩阵B赋值
            li = input().split()
            li = [int(v) for v in li]
            B.append(li)
        ans = [[0 for i in range(z)] for j in range(x)]  # 结果初始化3*5
        for i in range(x):
            for j in range(z):
                for k in range(y):
                    ans[i][j] += A[i][k] * B[k][j]
        for i in range(x):
            for j in range(z):
                if j == (z - 1):
                    print(ans[i][j])
                else:
                    print(ans[i][j], end=' ')
    except:
        break

# 方法二
while True:
    try:
        # 行数和列数
        x = int(input())
        y = int(input())
        z = int(input())
        # 矩阵A和矩阵B
        a = []
        b = []
        # 将输入的数据分别存到列表a和b中
        for i in range(x):
            a.append(list(map(int, input().split())))
        for i in range(y):
            b.append(list(map(int, input().split())))
        # 行--外围列表 最终结果行数由x决定，列表中生成len(x)个空列表用于存放最终结果
        res = [[] for _ in range(x)]
        # j将第一列作为列表中的第一个元组，第二列作为列表中的第二个元组
        # 矩阵a的列数和矩阵b的行数相同，将它们都放平了，列表a中第一个元素为矩阵a的第一行，
        # 列表b中第一个元素为矩阵b的第一列
        b = list(zip(*b))
        # 计算第i行第j列的元素
        for i in range(x):
            for j in range(z):
                sums = [n1 * n2 for n1, n2 in zip(a[i], b[j])]
                res[i].append(sum(sums))
        # 将结果一行一行输出
        for line in res:
            print(' '.join(map(str, line)))
    except:
        break
