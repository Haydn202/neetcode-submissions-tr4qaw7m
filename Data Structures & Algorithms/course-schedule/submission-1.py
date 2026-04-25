class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        preReqs = {}

        for c, p in prerequisites:
            if c in preReqs:
                preReqs[c].append(p)
            else:
                preReqs[c] = [p]
        
        visited = set()
        
        def dfs(c) -> bool:
            if c in visited:
                return True
            if c in path:
                return False

            path.add(c)
            for pre in preReqs.get(c, []):
                if not dfs(pre):
                    return False
            
            path.remove(c)
            visited.add(c)
            return True

        for i in range(numCourses):
            path = set()
            posible = dfs(i)
            if not posible:
                return False
        
        return True

        
