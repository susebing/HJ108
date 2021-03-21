# coding=utf-8
"""
题目描述
求给定二叉树的最大深度，
最大深度是指树的根结点到最远叶子结点的最长路径上结点的数量。

示例1
输入
复制
{1,2}
返回值
复制
2
示例2
输入
复制
{1,2,3,4,#,#,5}
返回值
复制
3
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @param root TreeNode类
# @return int整型
class Solution:
    def maxDepth(self, root):
        left_depth = 0
        right_depth = 0
        depth = 0
        if root is None:
            return depth
        if root.left is not None:
            left_depth += self.maxDepth(root.left)
        if root.right is not None:
            right_depth += self.maxDepth(root.right)
        if root.left is None and root.right is None:
            return 1
        if left_depth > right_depth:
            depth += left_depth
        else:
            depth += right_depth
        return depth + 1
