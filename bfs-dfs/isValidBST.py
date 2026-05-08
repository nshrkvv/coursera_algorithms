class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        to_list = []
        self.helper(root, to_list)
        is_bst = True
        prev = to_list[0] if to_list else None
        for i in range(1, len(to_list)):
            if to_list[i] <= prev:
                is_bst = False
                break
            prev = to_list[i]
        return is_bst
    def helper(self, node: Optional[TreeNode], to_list: List[int]) -> None:
        if node is None:
            return
        self.helper(node.left, to_list)
        to_list.append(node.val)
        self.helper(node.right, to_list)
