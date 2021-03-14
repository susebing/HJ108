# coding=utf-8
"""
题目描述
有一个数据表格为二维数组（数组元素为int类型），行长度为ROW_LENGTH,列长度为COLUMN_LENGTH。对该表格中数据的操作可以在单个单元内，也可以对一个整行或整列进行操作，操作包括交换两个单元中的数据；插入某些行或列。
请编写程序，判断对表格的各种操作是否合法。

详细要求:
1.数据表规格的表示方式为“行*列”, 数据表元素的位置表示方式为[行,列]，行列均从0开始编号
2.数据表的最大规格为9行*9列，对表格进行操作时遇到超出规格应该返回错误
3.插入操作时，对m*n表格，插入行号只允许0~m，插入列号只允许0~n。超出范围应该返回错误
4.只需记录初始表格中数据的变化轨迹，查询超出初始表格的数据应返回错误

例如:  初始表格为4*4，可查询的元素范围为[0,0]~[3,3]，假设插入了第2行，数组变为5*4，查询元素[4,0]时应该返回错误

输入描述:
输入数据按下列顺序输入：
1 表格的行列值
2 要交换的两个单元格的行列值
3 输入要插入的行的数值
4 输入要插入的列的数值
5 输入要获取运动轨迹的单元格的值

输出描述:
输出按下列顺序输出：
1 初始化表格是否成功，若成功则返回0， 否则返回-1
2 输出交换单元格是否成功
3 输出插入行是否成功
4 输出插入列是否成功
5 输出要查询的运动轨迹的单元查询是否成功

示例1
输入
复制
3 4
1 1
0 1
2
1
2 2
输出
复制
0
0
0
0
0
"""

# 题目看懂的难度大于程序本身。
# 乍一看，题目挺繁琐，实际上就是纸老虎，
# 就是检查每个输入参数是否超出给定范围，
# 是就输出-1，否就输出0

while True:
    try:
        x, y = map(int, input().split())
        # 判断初始化是否成功，即行列表是否超出规格
        if x > 9 or y > 9:
            print(-1)
        else:
            print(0)
        x1, y1, x2, y2 = map(int, input().split())
        # 判断交换单元格是否成功
        if x1 >= x or x2 >= x or y1 >= y or y2 >= y:
            print(-1)
        elif x1 == x2 and y1 == y2:
            print(-1)
        else:
            print(0)
        insertrow = int(input())
        # 判断插入行后是否超出范围
        if insertrow >= x or insertrow < 0 or x + 1 > 9:
            print(-1)
        else:
            print(0)
        insertcol = int(input())
        # 判断插入列后是否超出范围
        if insertcol >= y or insertcol < 0 or y + 1 > 9:
            print(-1)
        else:
            print(0)
        search = list(map(int, input().split()))
        # 判断查询的单元格是否存在
        if search[0] >= x or search[1] >= y:
            print(-1)
        else:
            print(0)
    except:
        break

# 方法二
"""
根据评论区讨论和样例说明，简单总结下题目要进行的操作：
1，数据表行列范围都是[0,9].
2，交换的坐标行列数要在输入的表格大小行列数范围[0, m)x[0, n)内.
3，插入的 x 位置要在 [0, m) 范围内，插入的 y 位置要在 [0, n) 范围内.
4，要检查的位置 (x,y) 要在 [0, m)x[0, n) 内.

以上条件若满足输出'0'，否则输出'-1'
"""

while True:
    try:
        # 数据表大小
        m, n = map(int, input().split())
        # 要交换的两个坐标位置
        x1, y1, x2, y2 = map(int, input().split())
        # 进行插入的行
        insert_x = int(input())
        # 进行插入的列
        insert_y = int(input())
        # 要查找的坐标位置
        x, y = map(int, input().split())

        # 1，数据表行列范围都是[0,9]，若满足输出'0'，否则输出'-1'
        if (0 <= m <= 9) and (0 <= n <= 9):
            print('0')
        else:
            print('-1')
        # 2，交换的坐标行列数要在输入的表格大小行列数范围[0, m)x[0, n)内
        if (0 <= x1 < m) and (0 <= y1 < n) and (0 <= x2 < m) and (0 <= y2 < n):
            print('0')
        else:
            print('-1')
        # 3.1，插入的x坐标要在 [0, m) 范围内
        if (0 <= insert_x < m) and (m < 9):
            print('0')
        else:
            print('-1')
        # 3.2，插入的y坐标要在 [0, n) 范围内
        if (0 <= insert_y < n) and (n < 9):
            print('0')
        else:
            print('-1')
        # 4，要检查的位置 (x,y) 要在 [0, m)x[0, n) 内
        if (0 <= x < m) and (0 <= y < n):
            print('0')
        else:
            print('-1')
    except:
        break
