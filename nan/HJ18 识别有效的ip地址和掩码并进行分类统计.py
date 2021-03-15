"""
题目描述
请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。

所有的IP地址划分为 A,B,C,D,E五类

A类地址1.0.0.0~126.255.255.255;

B类地址128.0.0.0~191.255.255.255;

C类地址192.0.0.0~223.255.255.255;

D类地址224.0.0.0~239.255.255.255；

E类地址240.0.0.0~255.255.255.255


私网IP范围是：

10.0.0.0～10.255.255.255

172.16.0.0～172.31.255.255

192.168.0.0～192.168.255.255


子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
注意二进制下全是1或者全是0均为非法

注意：
1. 类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时可以忽略
2. 私有IP地址和A,B,C,D,E类地址是不冲突的

输入描述:
多行字符串。每行一个IP地址和掩码，用~隔开。

输出描述:
统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。

示例1
输入
复制
10.70.44.68~255.254.255.0
1.0.0.1~255.0.0.0
192.168.0.2~255.255.255.0
19..0.~255.255.255.0
输出
复制
1 0 1 0 0 2 1
"""

# 255.255.255.255 为非法子网掩码（题目的意思，实际这个掩码，也能用）
# 当子网掩码错误时，不在判断ip是否有效，错误直接加一， 进行下次循环
# 当一个ip属于ABCDE类中的一个时候，也属于私有ip时，私有ip和他属于的分类都应该加一

# 思路：
# 首先呢，先判断子网掩码是否正确，方法是将子网掩码转换成32位0/1组成的二进制字符串，
# 那么怎样判断掩码合法呢，只需要判断该二进制中第一个0和最后一个1的位置即可，
# 只要第一个0在的位置比最后一个1的位置较前则掩码非法，
# 反则合法；然后如果掩码合法，接着判断IP是否合法，判断ip合法的方法很简单，就不赘述了


# 判断子网掩码是否存在非连续的1，（以下是所有连续1的情况）
lll = ['254', '252', '248', '240', '224', '192', '128', '0']
A, B, C, D, E, err, pri = 0, 0, 0, 0, 0, 0, 0


# 检测IP是否有效
def check_ip(ip):
    if len(ip) != 4 or " " in ip:
        return False
    else:
        for i in range(4):
            if int(ip[i]) < 0 or int(ip[i]) > 255:
                return False
        return True


def check_mask(ms):
    if len(ms) != 4:
        return False
    if ms[0] == '255':
        if ms[1] == '255':
            if ms[2] == '255':
                if ms[3] in lll:
                    return True
                else:
                    return False
            elif ms[2] in lll and ms[3] == '0':
                return True
            else:
                return False
        elif ms[1] in lll and ms[2] == ms[3] == '0':
            return True
        else:
            return False
    elif ms[0] in lll and ms[2] == ms[3] == ms[4] == '0':
        return True
    else:
        return False


# 主函数
while True:
    try:
        string = input().strip()
        list1 = string.split('~')[0]  # IP地址分割
        list2 = string.split('~')[1]  # 子网掩码分割
        ip = list1.split('.')
        ms = list2.split('.')
        if check_mask(ms) and check_ip(ip):
            if 1 <= int(ip[0]) <= 126:
                A += 1
            if 128 <= int(ip[0]) <= 191:
                B += 1
            if 192 <= int(ip[0]) <= 223:
                C += 1
            if 224 <= int(ip[0]) <= 239:
                D += 1
            if 240 <= int(ip[0]) <= 255:
                E += 1
            if int(ip[0]) == 10 or (int(ip[0]) == 172 and 15 < int(ip[1]) < 32) or (
                    int(ip[0]) == 192 and int(ip[1]) == 168):
                pri += 1
        else:
            err += 1
    except:
        break
print('%s %s %s %s %s %s %s' % (A, B, C, D, E, err, pri))
