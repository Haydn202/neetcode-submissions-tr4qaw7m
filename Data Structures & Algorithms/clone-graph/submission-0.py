"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = set()
        clones = {}

        def dfs(node: Node) -> node:
            if node in visited:
                return
            
            if node in clones:
                return clones[node]

            clone = Node(node.val)
            clones[node] = clone

            neighbors = []

            for neighbor in node.neighbors:
                neighbors.append(dfs(neighbor))

            clone.neighbors = neighbors

            #visited.add(node)

            return clone
        
        return dfs(node)
            




