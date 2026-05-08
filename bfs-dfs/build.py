from turtle import left


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        to_map = {}
        for i in range(len(inorder)):
            to_map[inorder[i]] = i
        return self.splitTree(preorder, to_map, 0, 0, len(inorder) - 1)

    def splitTree(self, preorder, to_map, rootIndex, left, right):
        if left > right:
            return None
        root = TreeNode(preorder[rootIndex])
        mid = to_map[preorder[rootIndex]]
        if mid > left:
            root.left = self.splitTree(preorder, to_map, rootIndex + 1, left, mid - 1)

        if mid < right:
            root.right = self.splitTree(preorder, to_map, rootIndex + mid - left + 1, mid + 1, right)
        return root
