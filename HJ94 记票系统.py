# coding=utf-8
"""
题目描述
请实现接口：
unsigned int  AddCandidate (char* pCandidateName);
功能：设置候选人姓名
输入： char* pCandidateName 候选人姓名
输出：无
返回：输入值非法返回0，已经添加过返回0 ，添加成功返回1

Void Vote(char* pCandidateName);
功能：投票
输入： char* pCandidateName 候选人姓名
输出：无
返回：无

unsigned int  GetVoteResult (char* pCandidateName);

功能：获取候选人的票数。如果传入为空指针，返回无效的票数，同时说明本次投票活动结束，释放资源
输入： char* pCandidateName 候选人姓名。当输入一个空指针时，返回无效的票数

输出：无
返回：该候选人获取的票数

void Clear()
// 功能：清除投票结果，释放所有资源
// 输入：
// 输出：无
// 返回

输入描述:
输入候选人的人数，第二行输入候选人的名字，第三行输入投票人的人数，第四行输入投票。

输出描述:
每行输出候选人的名字和得票数量。

示例1
输入
复制
4
A B C D
8
A B C D E F G H
输出
复制
A : 1
B : 1
C : 1
D : 1
Invalid : 4
"""

while True:
    try:
        a = int(input())
        b = input().split()
        c = int(input())
        d = input().split()
        e = {}
        for i in d:
            if i not in b:
                e["Invalid"] = e.get("Invalid", 0) + 1
            else:
                e[i] = e.get(i, 0) + 1
        for i in b:
            print(i, ":", e.get(i, 0))
        print("Invalid", ":", e.get("Invalid", 0))
    except:
        break
