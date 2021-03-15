# coding=utf-8
"""
题目描述
Jessi初学英语，为了快速读出一串数字，编写程序将数字转换成英文：

如22：twenty two，123：one hundred and twenty three。

说明：

数字为正整数，长度不超过九位，不考虑小数，转化结果为英文小写；

输出格式为twenty two；

非法数据请返回“error”；

关键字提示：and，billion，million，thousand，hundred。

方法原型：public static String parse(long num)

输入描述:
输入一个long型整数

输出描述:
输出相应的英文写法

示例1
输入
复制
2356
输出
复制
two thousand three hundred and fifty six
"""

num2word = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', \
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}


def thou(n):
    res = ''
    if n // 100 > 0:
        res += num2word[n // 100] + '    hundred  and  '
        n = n % 100
    if n > 0:
        if n < 19:
            res += num2word[n]
        else:
            res += num2word[n // 10 * 10] + '    '
            n = n % 10
            if n > 0:
                res += '   ' + num2word[n] + '    '
    return res


while True:
    try:
        n = int(input())
        m = n % 1000
        n = n // 1000
        res = thou(m)
        if n > 0:
            m = n % 1000
            n = n // 1000
            res = thou(m) + '  thousand   ' + res
        if n > 0:
            m = n % 1000
            n = n // 1000
            res = thou(m) + '  million   ' + res
        if n > 0:
            m = n % 1000
            n = n // 1000
            res = thou(m) + '  billion   ' + res
        print(" ".join(res.split()))
    except EOFError:
        break
