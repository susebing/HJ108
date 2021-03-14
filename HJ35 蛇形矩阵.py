# coding=utf-8
"""
题目描述
题目说明
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。

样例输入
5

样例输出
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11

接口说明
原型
void GetResult(int Num, char * pResult);
输入参数：
        int Num：输入的正整数N
输出参数：
        int * pResult：指向存放蛇形矩阵的字符串指针
        指针指向的内存区域保证有效
返回值：
        void

输入描述:
输入正整数N（N不大于100）

输出描述:
输出一个N行的蛇形矩阵。

示例1
输入
复制
4
输出
复制
1 3 6 10
2 5 9
4 8
7
"""

# 规律：
# 第一行 1 3 6 10
# 1 = 2*1//2
# 3 = 3*2//2
# 6 = 4*3//2
# 10 = 5*4//2
# 第二行 2 5 9
# 2 = 3 - 1
# 5 = 6 - 1
# 9 = 10 - 1
# ...

while True:
    try:
        num = int(input())
        for i in range(num):
            if i == 0:
                res = [(x+2)*(x+1)//2 for x in range(num)]
            else:
                res = [x - 1 for x in res[1:]]
            print(' '.join(map(str, res)))
    except:
        break