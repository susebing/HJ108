# coding=utf-8
"""
题目描述
开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。

处理：
1、 记录最多8条错误记录，循环记录（或者说最后只输出最后出现的八条错误记录），
对相同的错误记录（净文件名（保留最后16位）称和行号完全匹配）只记录一条，错误计数增加；

2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；

3、 输入的文件可能带路径，记录文件名称不能带路径。

输入描述:
一行或多行字符串。每行包括带路径文件名称，行号，以空格隔开。

输出描述:
将所有的记录统计并将结果输出，格式：文件名 代码行数 数目，一个空格隔开，如：

示例1
输入
复制
D:\zwtymj\xccb\ljj\cqzlyaszjvlsjmkwoqijggmybr 645
E:\je\rzuwnjvnuz 633
C:\km\tgjwpb\gy\atl 637
F:\weioj\hadd\connsh\rwyfvzsopsuiqjnr 647
E:\ns\mfwj\wqkoki\eez 648
D:\cfmwafhhgeyawnool 649
E:\czt\opwip\osnll\c 637
G:\nt\f 633
F:\fop\ywzqaop 631
F:\yay\jc\ywzqaop 631

输出
复制
rzuwnjvnuz 633 1
atl 637 1
rwyfvzsopsuiqjnr 647 1
eez 648 1
fmwafhhgeyawnool 649 1
c 637 1
f 633 1
ywzqaop 631 2
"""

# 注意：
# 这道题不能再最外面加while: try： except:

arr = []
res = {}
while 1:
    try:
        path, line = input().split()
        name = path.split('\\')[-1]
        if len(name) > 16:
            name = name[-16:]
        k = name + line
        if k in res:
            res[k] += 1
        else:
            res[k] = 1
            # 相同 k 只记录一次，所有这个地方存 k
            arr.append((name, line, k))
    except:
        break
for name, line, k in arr[-8:]:
    print(f'{name} {line} {res[k]}')
