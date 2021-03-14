"""
题目描述
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。
从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

输入：

合法坐标为A(或者D或者W或者S) + 数字（两位以内）
坐标之间以;分隔。
非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。

下面是一个简单的例子 如：
A10;S20;W10;D30;X;A1A;B10A11;;A10;

处理过程：

起点（0,0）
+   A10   =  （-10,0）
+   S20   =  (-10,-20)
+   W10  =  (-10,-10)
+   D30  =  (20,-10)
+   x    =  无效
+   A1A   =  无效
+   B10A11   =  无效
+  一个空 不影响
+   A10  =  (10,-10)

结果 （10， -10）

注意请处理多组输入输出

输入描述:
一行字符串
输出描述:
最终坐标，以,分隔
示例1
输入
复制
A10;S20;W10;D30;X;A1A;B10A11;;A10;
输出
复制
10,-10
"""

# //思路：
# //1 分割字符串
# //2 判断分割后的字符串坐标是否合法
# //3 对合法的字符串坐标判断方向，并将字符串中的数字提取出来，在前面的坐标基础上进行运算
# //4 确定运算规则：初始坐标（x,y）===>
# //字符串为Anum===》x-=num
# //字符串为Snum===》y-=num
# //字符串为Wnum===》y+=num
# //字符串为Dnum===》x+=num

# 方法一 耗时更少
while True:
    try:
        data = input().split(';')
        start = [0, 0]
        for per in data:
            if not per:
                continue
            try:
                if per[0] == 'A':
                    start[0] -= int(per[1:])
                elif per[0] == 'D':
                    start[0] += int(per[1:])
                elif per[0] == 'W':
                    start[1] += int(per[1:])
                elif per[0] == 'S':
                    start[1] -= int(per[1:])
            except:
                continue
        print(str(start[0]) + ',' + str(start[1]))
    except:
        break

# 方法二 耗时大
import re

while 1:
    try:
        point = [0, 0]
        arr = input().split(';')
        for item in arr:
            if re.search('^[ASWD]\d+$', item):
                if item.startswith('A'):
                    point[0] -= int(item[1:])
                if item.startswith('S'):
                    point[1] -= int(item[1:])
                if item.startswith('W'):
                    point[1] += int(item[1:])
                if item.startswith('D'):
                    point[0] += int(item[1:])
        print(f"{point[0]},{point[1]}")
    except:
        break

