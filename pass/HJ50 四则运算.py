# coding=utf-8
"""
题目描述
请实现如下接口
    /* 功能：四则运算
     * 输入：strExpression：字符串格式的算术表达式，如: "3+2*{1+2*[-4/(8-6)+7]}"
         * 返回：算术表达式的计算结果
     */
    public static int calculate(String strExpression)
    {
        /* 请实现*/
        return 0;
    }
约束：
pucExpression字符串中的有效字符包括[‘0’-‘9’],‘+’,‘-’, ‘*’,‘/’ ,‘(’， ‘)’,‘[’, ‘]’,‘{’ ,‘}’。
pucExpression算术表达式的有效性由调用者保证;

输入描述:
输入一个算术表达式

输出描述:
得到计算结果

示例1
输入
复制
3+2*{1+2*[-4/(8-6)+7]}
输出
复制
25
"""

while True:
    try:
        print(eval(input()))
    except:
        break
