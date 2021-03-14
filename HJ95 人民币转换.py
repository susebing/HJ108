# coding=utf-8
"""
题目描述
考试题目和要点：
1、中文大写金额数字前应标明“人民币”字样。中文大写金额数字应用壹、贰、叁、肆、伍、陆、柒、捌、玖、拾、佰、仟、万、亿、元、角、分、零、整等字样填写。（30分）
2、中文大写金额数字到“元”为止的，在“元”之后，应写“整字，如￥ 532.00应写成“人民币伍佰叁拾贰元整”。在”角“和”分“后面不写”整字。（30分）
3、阿拉伯数字中间有“0”时，中文大写要写“零”字，阿拉伯数字中间连续有几个“0”时，中文大写金额中间只写一个“零”字，如￥6007.14，应写成“人民币陆仟零柒元壹角肆分“。（40分）

输入描述:
输入一个double数

输出描述:
输出人民币格式

示例1
输入
复制
151121.15
输出
复制
人民币拾伍万壹仟壹佰贰拾壹元壹角伍分
"""


def fun(arr):
    # m = '0,1,2,3,4,5,6,7,8,9'.split(',')
    n = '零,壹,贰,叁,肆,伍,陆,柒,捌,玖'.split(',')
    p = '仟,佰,拾,亿,仟,佰,拾,万,仟,佰,拾,元'.split(',')
    q = '角,分'.split(',')
    z = arr[0]  # 整数部分
    res_z = '人民币'
    x = arr[1]  # 小数部分
    res_x = ''

    # 处理小数部分
    for i in range(len(x)):
        if x[i] == '0':
            res_x += ''
        else:
            res_x += n[int(x[i])] + q[i]
    # 处理整数部分
    for i in range(len(z)):
        if z[i] == '0' and res_z[-1] != '拾':
            res_z += '零'
        elif z[i] == '0' and res_z[-1] == '拾':
            res_z += '零' + p[i - len(z)]
        else:
            res_z += n[int(z[i])] + p[i - len(z)]
    # 调整输出文字
    res_z = res_z.replace('零零', '零')
    res_z = res_z.replace('零零', '零')
    #        res_z = res_z[:-1] + res_z[-1].replace('零', '元')
    res_z = res_z.replace('拾零', '拾')
    res_z = res_z.replace('壹拾', '拾')
    res_z = res_z.replace('人民币零', '人民币')
    if res_z[-1] == '零':
        res_z = res_z[:-1] + res_z[-1].replace('零', '元')

    # 1，若有整数和小数
    if res_x:
        return res_z + res_x
    # 2，若只有整数
    else:
        return res_z + '整'


while True:
    try:
        rmb = input().strip().split('.')
        print(fun(rmb))
    except:
        break
