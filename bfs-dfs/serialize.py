class Codec:
    def serialize(self, root):
        if not root: 
            return
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            if node:
                result.append (str(node.val))
                queue. append (node. left)
                queue. append(node.right)
            else:
                result.append("N" )
        return ",". join(result)
