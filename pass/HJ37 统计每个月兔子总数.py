# coding=utf-8
"""
题目描述
有一只兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子，
假如兔子都不死，问每个月的兔子总数为多少？

/**
* 统计出兔子总数。
*
* @param monthCount 第几个月
* @return 兔子总数
*/
public static int getTotalCount(int monthCount)
{
return 0;
}

本题有多组数据，请使用while (cin>>)读取

输入描述:
输入int型表示month

输出描述:
输出兔子总数int型

示例1
输入
复制
9
输出
复制
34
"""

# 相当于求 1 1 2 3 5 8 13
# 后一个月等于前两个月之和

while True:
    try:
        month = int(input())
        a, b = 1, 0
        for i in range(month):
            a, b = b, a + b
        print(b)
    except:
        break
