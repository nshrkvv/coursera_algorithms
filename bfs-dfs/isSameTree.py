class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False
        left_check = self.isSameTree(p.left, q.left)
        right_check = self.isSameTree(p.right, q.right)
        return left_check and right_check