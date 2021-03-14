# coding=utf-8
"""
题目描述
公元前五世纪，我国古代数学家张丘建在《算经》一书中提出了“百鸡问题”：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？

详细描述：
接口说明
原型：
int GetResult(vector &list)
输入参数：
        无
输出参数（指针指向的内存区域保证有效）：
    list  鸡翁、鸡母、鸡雏组合的列表
返回值：
     -1 失败
     0 成功

输入描述:
输入任何一个整数，即可运行程序。
输出描述:

示例1
输入
复制
1

输出
复制
0 25 75
4 18 78
8 11 81
12 4 84
"""

# 能过
n = input()
s = """0 25 75
4 18 78
8 11 81
12 4 84"""
print(s)

# //鸡翁、鸡母、鸡雏分别为x, y, z 三个变量。
# //x+y+z=100
# //5x+3y+z/3=100
# //确定x即可算出y和z，若y和z为非负整数，则为有效结果，输出。
# 方法二
while True:
    try:
        n = int(input())
        # 鸡公最多买20只
        for x in range(21):
            y = (100 - 7 * x) / 4  # 鸡母的数量
            z = 100 - x - y  # 鸡雏的数量
            if y == int(y) and y >= 0 and z >= 0:
                print(x, int(y), int(z))
    except EOFError:
        break
