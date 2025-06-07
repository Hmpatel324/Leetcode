"""
Link: https://leetcode.com/problems/max-area-of-island/
Difficulty: medium

Problem:
Find the area of the largest island in a graph

Input / Output:


Notes:


Solution Approaches:
Iterative BFS apprach
Optimizations:
    No set for tracking needed if you update land cells to water in exploration
    use range in the parent to iterate over the grid

"""
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        if not grid: return res
        r_max, c_max = len(grid), len(grid[0])
        def bfsHelper(r_in, c_in):
            grid[r_in][c_in]=0
            queue = [(r_in, c_in)]
            area = 0
            while queue:
                r,c = queue.pop(0)
                area += 1
                for n_r, n_c in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if 0<=n_r<r_max and 0<=n_c<c_max and grid[n_r][n_c]==1:
                        grid[n_r][n_c] = 0
                        queue.append((n_r, n_c))
            return area
        for x in range(r_max):
            for y in range(c_max):
                if grid[x][y]==1:
                    a = bfsHelper(x,y)
                    res = max(res, a)
        return res
