# coding=utf-8
"""
题目描述
如果统计的个数相同，则按照ASCII码由小到大排序输出 。如果有其他字符，则对这些字符不用进行统计。

实现以下接口：
输入一个字符串，对字符中的各个英文字符，数字，空格进行统计（可反复调用）
按照统计个数由多到少输出统计结果，如果统计的个数相同，则按照ASCII码由小到大排序输出
清空目前的统计结果，重新统计
调用者会保证：
输入的字符串以‘\0’结尾。

输入描述:
输入一串字符。

输出描述:
对字符中的
各个英文字符（大小写分开统计），数字，空格进行统计，并按照统计个数由多到少输出,如果统计的个数相同，则按照ASII码由小到大排序输出 。如果有其他字符，则对这些字符不用进行统计。

示例1
输入
复制
aadddccddc
输出
复制
dca
"""

# 字符统计：大小写字母，数字，空格,
# 并按照出现的次数由大到小输出
# 思路：先数组统计出现的字符及个数，然后用multimap存储，输出时先存储到栈中在输出

# isalpha   大小写字母
# isdigit   数字
# isspace   空格

while True:
    try:
        list1 = []
        arr = input()
        dic = {}
        for i in arr:
            if i.isalpha() or i.isdigit() or i.isspace():
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i] = 1
        dic = sorted(dic.items(), key=lambda x: x[0])  # 先按字符ASC排
        dic = sorted(dic, key=lambda x: x[1], reverse=True)  # 再按统计数目排
        print(''.join(k for (k, v) in dic))
    except:
        break
