# coding=utf-8
"""
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 二叉树：[3,9,20,null,null,15,7],

arr = ['3', '9', '20', 'null', 'null', '15', '7']
arr = ['0'] + arr
res = []
i = 0
while True:
    if 2 ** (i + 1) < len(arr):
        temp = [item for item in arr[2 ** i:2 ** (i + 1)] if item != 'null']
        res.append(temp)
    else:
        temp = [item for item in arr[2 ** i:] if item != 'null']
        res.append(temp)
        break
    i += 1
print(res)
