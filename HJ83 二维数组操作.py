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
