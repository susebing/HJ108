# coding=utf-8
"""
题目描述
分别按照二叉树先序，中序和后序打印所有的节点。
示例1
输入
复制
{1,2,3}
返回值
复制
[[1,2,3],[2,1,3],[2,3,1]]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.res = [[], [], []]

    def threeOrders(self, root_node):
        self.dfs(root_node)
        return self.res

    def dfs(self, root_node):
        if root_node is None:
            return False
        # 根
        self.res[0].append(root_node.val)
        # 左
        self.dfs(root_node.left)
        self.res[1].append(root_node.val)
        # 右
        self.dfs(root_node.right)
        self.res[2].append(root_node.val)
        return True


if __name__ == '__main__':
    root = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(3)
    n3 = TreeNode(4)
    n4 = TreeNode(5)
    root.left = n1
    root.right = n2
    n2.left = n3
    n2.right = n4

    s = Solution()
    print(s.threeOrders(root))
