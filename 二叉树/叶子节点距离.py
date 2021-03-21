# coding=utf-8
"""
输入：root = [4,9,0,5,1]
输出：1026
解释：
从根到叶子节点路径 4->9->5 代表数字 495
从根到叶子节点路径 4->9->1 代表数字 491
从根到叶子节点路径 4->0 代表数字 40
因此，数字总和 = 495 + 491 + 40 = 1026

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 深度优先搜索
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        node = root
        Stack = []
        final = 0
        while node or Stack:
            # print(final)
            if Stack:  # 初始判定
                temp = Stack[-1][1]
            else:
                temp = 0
            if node:  # 入栈
                Stack.append([node, temp * 10 + node.val])
            if node and node.left:  # 当左儿子
                node = node.left
            elif node and node.right:  # 当右儿子
                node = node.right
            else:  # 没有左右
                if node:  # 并且是叶子节点，final累加
                    final += Stack[-1][1]
                Stack.pop()  # 将叶子节点弹出
                while 1:  # 第6条和第7条。无限循环。
                    if Stack and Stack[-1][0].left == node and Stack[-1][0].right:  # 我是左二子，爸爸还有右儿子。
                        node = Stack[-1][0].right
                        break
                    elif Stack:  # 我就是爸爸的右儿子。
                        node = Stack.pop()[0]
                    else:  # 全查完了。收摊。
                        node = None
                        break
        return final


if __name__ == '__main__':
    root = TreeNode(4)
    n1 = TreeNode(9)
    n2 = TreeNode(0)
    n3 = TreeNode(5)
    n4 = TreeNode(1)
    root.left = n1
    root.right = n2
    n1.left = n3
    n1.right = n4

    s = Solution()
    print(s.sumNumbers(root))
