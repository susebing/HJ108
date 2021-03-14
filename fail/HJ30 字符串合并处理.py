# coding=utf-8
"""
题目描述
按照指定规则对输入的字符串进行处理。

详细描述：
将输入的两个字符串合并。
对合并后的字符串进行排序，

要求为：下标为奇数的字符和下标为偶数的字符分别从小到大排序。
这里的下标意思是字符在字符串中的位置。

对排序后的字符串进行操作，如果字符为‘0’——‘9’或者‘A’——‘F’或者‘a’——‘f’，
则对他们所代表的16进制的数进行BIT倒序的操作，并转换为相应的大写字符。

如字符为‘4’，为0100b，则翻转后为0010b，也就是2。
转换后的字符为‘2’；

如字符为‘7’，为0111b，则翻转后为1110b，也就是e。
转换后的字符为大写‘E’。

举例：输入str1为"dec"，str2为"fab"，合并为“decfab”，分别对“dca”和“efb”进行排序，排序后为“abcedf”，转换后为“5D37BF”
接口设计及说明：
/*
功能:字符串处理
输入:两个字符串,需要异常处理
输出:合并处理后的字符串，具体要求参考文档
返回:无
*/
void ProcessString(char* str1,char *str2,char * strOutput)
{
}

输入描述:
输入两个字符串

输出描述:
输出转化后的结果

示例1
输入
复制
dec fab
输出
复制
5D37BF
"""

hex_num = ['0', '1', '2', '3',
           '4', '5', '6', '7',
           '8', '9', 'a', 'b',
           'c', 'd', 'e', 'f',
           'A', 'B', 'C', 'D',
           'E', 'F']


def helper(s):
    ten = int(s, 16)
    bc = format(ten, 'b').rjust(4, '0')
    bc = list(bc)
    bc.reverse()
    ten = int(''.join(bc), 2)
    hc = format(ten, 'x')
    return hc.upper()


while True:
    try:
        a, b = input().strip().split()
        res = list(a + b)
        res[::2] = sorted(res[::2])
        res[1::2] = sorted(res[1::2])
        for i in range(len(res)):
            if res[i] in hex_num:
                res[i] = helper(res[i])
        print(''.join(res))
    except EOFError:
        break


# 方法二

def func():
    s = input().replace(' ', '')
    # 取奇偶位
    i = 0
    sj = ''
    so = ''
    for c in s:
        if i % 2 == 0:
            so += c
        else:
            sj += c
        i += 1
    # 分别排序
    so = ''.join(sorted(so))
    sj = ''.join(sorted(sj))
    # 排序后再次合并
    s = ''
    while True:
        s += so[:1]
        s += sj[:1]
        so = so[1:]
        sj = sj[1:]
        if not so and not sj:
            break
    # 查表
    dic1 = '0123456789abcdef'
    dic2 = '084C2A6E195D3B7F'
    r = ''
    for c in s:
        if c.lower() not in dic1:
            r += c
            continue
        r += dic2[dic1.find(c.lower())]
    print(r)


while True:
    try:
        func()
    except:
        break

# 方法三
while True:
    try:
        s = input().replace(" ", "")
        ss = ""
        dic = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        odd, even = "", ""
        for i, v in enumerate(s):
            if i % 2 == 0:
                even += v
            else:
                odd += v
            odd = "".join(sorted(odd))
            even = "".join(sorted(even))

        for i in range(len(even)):
            if even[i] in "0123456789abcdefABCDEF":
                ss += dic[int(bin(dic.index(even[i].upper())).replace("0b", "").rjust(4, "0")[::-1], 2)]
            else:
                ss += even[i]
            if len(odd) != i:
                if odd[i] in "0123456789abcdefABCDEF":
                    ss += dic[int(bin(dic.index(odd[i].upper())).replace("0b", "").rjust(4, "0")[::-1], 2)]
                else:
                    ss += odd[i]
        print(ss)
    except:
        break
