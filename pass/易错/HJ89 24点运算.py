# coding=utf-8
"""
题目描述
计算24点是一种扑克牌益智游戏，随机抽出4张扑克牌，通过加(+)，减(-)，乘(*), 除(/)四种运算法则计算得到整数24，本问题中，扑克牌通过如下字符或者字符串表示，其中，小写joker表示小王，大写JOKER表示大王：
                   3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER

本程序要求实现：输入4张牌，输出一个算式，算式的结果为24点。
详细说明：

1.运算只考虑加减乘除运算，没有阶乘等特殊运算符号，友情提醒，整数除法要当心；
2.牌面2~10对应的权值为2~10, J、Q、K、A权值分别为为11、12、13、1；
3.输入4张牌为字符串形式，以一个空格隔开，首尾无空格；如果输入的4张牌中包含大小王，则输出字符串“ERROR”，表示无法运算；
4.输出的算式格式为4张牌通过+-*/四个运算符相连，中间无空格，4张牌出现顺序任意，只要结果正确；
5.输出算式的运算顺序从左至右，不包含括号，如1+2+3*4的结果为24
6.如果存在多种算式都能计算得出24，只需输出一种即可，如果无法得出24，则输出“NONE”表示无解。

输入描述:
输入4张牌为字符串形式，以一个空格隔开，首尾无空格；

输出描述:
如果输入的4张牌中包含大小王，则输出字符串“ERROR”，表示无法运算；
示例1
输入
复制
A A A A
输出
复制
NONE
"""
# 方法一
# 思路：对所有数字全排列，计算每种排列能否凑成24（题目默认按照先后顺序计算，即（(a+b)+c))+d模式。
# 如果joker 或 JOKER 在输入序列中，返回ERROR
# 当有一个满足的解时，返回；遍历完所有排列，如果没有满足的解，返回NONE
from itertools import permutations

while True:
    try:
        def game24(pokers):
            dic = {'A': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': '10',
                   'J': '11', 'Q': '12', 'K': '13'}
            ops = r'+-*/'
            exp = '((%s %s %s) %s %s )%s %s'  ## 这道题默认括号是这么加的
            for a in permutations(pokers):  ## nums 的全排列
                for op1 in ops:
                    for op2 in ops:
                        for op3 in ops:
                            t = exp % (dic[a[0]], op1, dic[a[1]], op2, dic[a[2]], op3, dic[a[3]]) if check(
                                exp % (dic[a[0]], op1, dic[a[1]], op2, dic[a[2]], op3, dic[a[3]])) else False
                            if t:  ## 这题只需要求出一个满足要求的等式即可
                                result = a[0] + op1 + a[1] + op2 + a[2] + op3 + a[3]
                                return result
            return 'NONE'


        def check(exp):  # 为了排除中间/0的情况，并且若等式值为24，返回True
            try:
                return int(eval(exp) == 24)
            except:
                return False


        pokers = input().split(' ')
        if 'joker' in pokers or 'JOKER' in pokers:
            print('ERROR')
        else:
            print(game24(pokers))
    except:
        break

# 方法二
# poke dictionary
pokedict = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
operators = ['+', '-', '*', '/']


def calto_24(pokeget):  # type<pokrget>==list
    outpoke = []  # output poke list
    if 'joker' in pokeget or 'JOKER' in pokeget:
        print('ERROR')
    else:
        pokelist = []
        for ss in pokeget:
            if ss in pokedict:
                pokelist.append(pokedict[ss])
            else:
                pokelist.append(int(ss))
        for i in range(4):
            for j in range(4):
                if j != i:
                    for k in range(4):
                        if k not in [i, j]:
                            indexs = [0, 1, 2, 3]  # index list
                            indexs.remove(i)
                            indexs.remove(j)
                            indexs.remove(k)
                            m = indexs[0]
                            for op1 in operators:
                                if op1 == '+': answer1 = pokelist[i] + pokelist[j]
                                if op1 == '-': answer1 = pokelist[i] - pokelist[j]
                                if op1 == '*': answer1 = pokelist[i] * pokelist[j]
                                if op1 == '/': answer1 = pokelist[i] / pokelist[j]
                                for op2 in operators:
                                    if op2 == '+': answer2 = answer1 + pokelist[k]
                                    if op2 == '-': answer2 = answer1 - pokelist[k]
                                    if op2 == '*': answer2 = answer1 * pokelist[k]
                                    if op2 == '/': answer2 = answer1 / pokelist[k]
                                    for op3 in operators:
                                        if op3 == '+': answer3 = answer2 + pokelist[m]
                                        if op3 == '-': answer3 = answer2 - pokelist[m]
                                        if op3 == '*': answer3 = answer2 * pokelist[m]
                                        if op3 == '/': answer3 = answer2 / pokelist[m]
                                        if answer3 == 24:
                                            outpoke.append(
                                                pokeget[i] + op1 + pokeget[j] + op2 + pokeget[k] + op3 + pokeget[m])
        if len(outpoke) == 0:
            print('NONE')
        else:
            for o in outpoke: print(o)


inpoke = input().split()
calto_24(inpoke)
