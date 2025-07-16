"""
Link: https://leetcode.com/problems/rotting-oranges
Difficulty: mediun

Problem:
Given a grid (0 - empty, 1 - fresh, 2 rotting)
return number of cycles for all to be rotten or -1 if impossible
rotting makes all neighbors rotting

Input / Output:


Notes:


Solution Approaches:

"""
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0

        total = 0
        queue = []
        r_max, c_max = len(grid), len(grid[0])

        for i in range(r_max):
            for j in range(c_max):
                if grid[i][j]!=0: total+=1
                if grid[i][j]==2: queue.append((i,j))
        if total==0: return 0
        def bfs(queue):
            res = -1
            visited = set()
            visited.update(queue)
            while queue:
                res+=1
                temp = []
                for r,c in queue:
                    for n_r,n_c in [(r-1,c),(r+1,c),(r,c+1),(r,c-1)]:
                        if 0<=n_r<r_max and 0<=n_c<c_max and (n_r,n_c) not in visited and grid[n_r][n_c]==1:
                            visited.add((n_r,n_c))
                            temp.append((n_r,n_c))
                queue = temp
            return res if len(visited)==total else -1   
        return bfs(queue)
