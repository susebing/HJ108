# coding=utf-8
"""
题目描述
输入整型数组和排序标识，对其元素按照升序或降序进行排序（一组测试用例可能会有多组数据）
接口说明
原型：
void sortIntegerArray(Integer[] pIntegerArray, int iSortFlag);
输入参数：
Integer[] pIntegerArray：整型数组
int  iSortFlag：排序标识：0表示按升序，1表示按降序
输出参数：
无
返回值：
void
本题有多组输入，请使用while(cin>>)处理

输入描述:
1、输入需要输入的整型数个数

输出描述:
输出排好序的数字

示例1
输入
复制
8
1 2 4 9 3 55 64 25
0
输出
复制
1 2 3 4 9 25 55 64
"""

while True:
    try:
        a = int(input())
        b = list(map(int, input().split()))
        c = int(input())
        ans = sorted(b, reverse=c)
        res = ''
        for i in ans:
            res = res + str(i) + " "
        print(res)
    except:
        break
