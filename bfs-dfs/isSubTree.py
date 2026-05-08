class Solution:
    def isSubTree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if subRoot is None:
            return True
        if root is None and subRoot != 0:
            return False
        if self.isSameTree(root, subRoot):
            return True
        left_check = self.isSubTree(root.left, subRoot)
        right_check = self.isSubTree(root.right, subRoot)
        return left_check or right_check
