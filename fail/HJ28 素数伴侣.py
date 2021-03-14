# coding=utf-8
"""
题目描述
题目描述
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，
如2和5、6和13，它们能应用于通信加密。

现在密码学会请你设计一个程序，从已有的N（N为偶数）个正整数中挑选出若干对组成“素数伴侣”，

挑选方案多种多样，
例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，
而将2和5、6和13编组将得到两组“素数伴侣”，
能组成“素数伴侣”最多的方案称为“最佳方案”，
当然密码学会希望你寻找出“最佳方案”。

输入:
有一个正偶数N（N≤100），表示待挑选的自然数的个数。后面给出具体的数字，范围为[2,30000]。

输出:
输出一个整数K，表示你求得的“最佳方案”组成“素数伴侣”的对数。

输入描述:
输入说明
1 输入一个正偶数n
2 输入n个整数

输出描述:
求得的“最佳方案”组成“素数伴侣”的对数。

示例1
输入
复制
4
2 5 6 13
输出
复制
2
"""
n = 60000
prime = []
for i in range(n + 1):
    prime.append(True)
for i in range(2, n + 1):
    if prime[i]:
        j = i + i
        while j <= n:
            prime[j] = False
            j += i
while 1:
    try:
        n = int(input())
        s = list(map(int, input().split()))
        odd = [x for x in s if x % 2 != 0]
        even = [x for x in s if x % 2 == 0]
        arr2 = [[] for i in range(len(even))]
        count = 0
        for i in range(len(odd)):
            for j in range(len(even)):
                if prime[odd[i] + even[j]]:
                    arr2[j].append(odd[i])
        arr2.sort(key=lambda s: len(s))
        for i in range(len(even)):
            if arr2[i] != []:
                count = count + 1
                temp = arr2[i][0]
                for k in range(len(even)):
                    if temp in arr2[k]:
                        arr2[k].remove(temp)
            arr2.sort(key=lambda s: len(s))
        print(count)
    except:
        break


# 方法二
def issu(x):
    tem = 2
    while tem ** 2 <= x:
        if x % tem == 0:
            return False
        tem += 1
    return True


def find(a, list1, list2, list3):
    for i in range(len(list3)):
        if issu(a + list3[i]) and list1[i] == 0:
            list1[i] = 1
            if list2[i] == 0 or find(list2[i], list1, list2, list3):
                list2[i] = a
                return True
    return False


while True:
    try:
        n = int(input())
        l = list(map(int, input().strip().split()))
        odd = []
        even = []
        for i in range(n):
            if l[i] % 2 == 0:
                even.append(l[i])
            else:
                odd.append(l[i])
        count = 0
        match = [0] * len(even)
        for i in range(len(odd)):
            used = [0] * len(even)
            if find(odd[i], used, match, even):
                count += 1
        print(count)
    except:
        break
