class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        to_list = []
        self.helper(root, to_list)
        return to_list[k - 1]

    def helper(self, node, to_list):
        if node is None:
            return
        self.helper(node.left, to_list)
        to_list.append(node.val)
        self.helper(node.right, to_list)
