class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            max_sum = max(max_sum, left + right + node.val)
            return max(left, right) + node.val
        
        dfs(root)
        return max_sum
