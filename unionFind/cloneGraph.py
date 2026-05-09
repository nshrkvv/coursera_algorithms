class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        cloned_nodes = {}
        queue = [node]
        cloned_nodes[node] = Node(node.val)
        while queue:
            curr = queue.pop(0)
            for neighbor in curr.neighbors:
                if neighbor not in cloned_nodes:
                    cloned_nodes[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                cloned_nodes[curr].neighbors.append(cloned_nodes[neighbor])
        return cloned_nodes[node]
