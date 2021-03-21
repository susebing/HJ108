# coding=utf-8
"""
题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。
比如：    源二叉树
            8
           /  \
          6   10
         / \  / \
        5  7 9 11
        镜像二叉树
            8
           /  \
          10   6
         / \  / \
        11 9 7  5
示例1
输入
复制
{8,6,10,5,7,9,11}
返回值
复制
{8,10,6,11,9,7,5}
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return TreeNode类
#
class Solution:
    def Mirror(self, pRoot):
        # write code here
        if pRoot:
            right = self.Mirror(pRoot.left)
            left = self.Mirror(pRoot.right)
            pRoot.left = left
            pRoot.right = right
            return pRoot
