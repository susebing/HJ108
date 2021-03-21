# coding=utf-8
"""
题目描述
给定彼此独立的两棵二叉树，判断 t1 树是否有与 t2 树拓扑结构完全相同的子树。
设 t1 树的边集为 E1，t2 树的边集为 E2，若 E2 等于 E1 ，则表示 t1 树和t2 树的拓扑结构完全相同。
示例1
输入
复制
{1,2,3,4,5,6,7,#,8,9},{2,4,5,#,8,9}
返回值
复制
true
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @param root1 TreeNode类
# @param root2 TreeNode类
# @return bool布尔型
class Solution:
    def isContains(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return self.isSame(root1, root2) \
               or self.isContains(root1.left, root2) \
               or self.isContains(root1.right, root2)

    def isSame(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return root1.val == root2.val \
               and self.isSame(root1.left, root2.left) \
               and self.isSame(root1.right, root2.right)
