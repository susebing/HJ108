# coding=utf-8
"""
题目描述
给定一个二叉树和一个值\ sum sum，请找出所有的根节点到叶子节点的节点值之和等于\ sum sum 的路径，
例如：
给出如下的二叉树，\ sum=22 sum=22，

返回
[
[5,4,11,2],
[5,8,9]
]

示例1
输入
复制
{1,2},1
返回值
复制
[]

示例2
输入
复制
{1,2},3
返回值
复制
[[1,2]]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @param root TreeNode类
# @param sum int整型
# @return int整型二维数组
#
def backtracking(root, ans, path, sum):
    if not root.left and not root.right:
        if sum == root.val:
            ans.append(path + [root.val])
        return
    path.append(root.val)
    if root.left:
        backtracking(root.left, ans, path, sum - root.val)
    if root.right:
        backtracking(root.right, ans, path, sum - root.val)
    path.pop()


class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []
        # write code
        ans = []
        backtracking(root, ans, [], sum)
        return ans
