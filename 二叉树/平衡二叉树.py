# coding=utf-8
"""
题目描述
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
平衡二叉树（Balanced Binary Tree），
具有以下性质：
它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，
并且左右两个子树都是一棵平衡二叉树。

示例1
输入
复制
{1,2,3,4,5,6,7}
返回值
复制
true
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = True

    def IsBalanced_Solution(self, root):
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return 0
        if not self.res:
            return 1
        left = 1 + self.helper(root.left)
        right = 1 + self.helper(root.right)
        if abs(left - right) > 1:
            self.res = False
        return max(left, right)
