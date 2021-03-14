# coding=utf-8
"""
题目描述
将一个字符中所有出现的数字前后加上符号“*”，其他字符保持不变
public static String MarkNum(String pInStr)
{
return null;
}
注意：输入数据可能有多行
输入描述:
输入一个字符串

输出描述:
字符中所有出现的数字前后加上符号“*”，其他字符保持不变

示例1
输入
复制
Jkdi234klowe90a3
输出
复制
Jkdi*234*klowe*90*a*3*
"""

# 将数字周围都加上*  两个数字中间肯定有两个** 然后替换掉就行了
# 正则 sub + lambda 替换，非常简单

import re

while 1:
    try:
        s = input()
        a = re.sub('\d+', lambda x: x.group(0).replace(x.group(0), f'*{x.group(0)}*'), s)
        print(a)
    except:
        break

# 方法二
import re

while 1:
    try:
        print(re.sub('(\d+)', '*\g<1>*', input()))
    except:
        break
