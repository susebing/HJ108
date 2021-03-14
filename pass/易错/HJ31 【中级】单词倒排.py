# coding=utf-8
"""
题目描述
对字符串中的所有单词进行倒排。
说明：
1、构成单词的字符只有26个大写或小写英文字母；
2、非构成单词的字符均视为单词间隔符；
3、要求倒排后的单词间隔符以一个空格表示；如果原字符串中相邻单词间有多个间隔符时，倒排转换后也只允许出现一个空格间隔符；
4、每个单词最长20个字母；

输入描述:
输入一行以空格来分隔的句子

输出描述:
输出句子的逆序

示例1
输入
复制
I am a student
输出
复制
student a am I
"""

# Python isalpha() 方法检测字符串是否只由字母组成。

while 1:
    try:
        s = input()
        new_s = ''
        for c in s:
            if c.isalpha():
                new_s += c
            else:
                new_s += ' '
        new_line = new_s.split()[::-1]
        print(' '.join(new_line))
    except:
        break
