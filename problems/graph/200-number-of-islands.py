"""
Link: https://leetcode.com/problems/number-of-islands
Difficulty: medium

Problem:
Find number of islands in a grid

Input / Output:


Notes:


Solution Approaches:
Utilize BFS algo for exploration of initial land cell. 
Within exploration, mark adjacent land as sea so that entire island counts as 1 land mass.

"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        r_max, c_max = len(grid), len(grid[0])
        res = 0
        
        def helper(r_in, c_in):
            visited = set()
            queue = [(r_in, c_in)]
            while queue:
                r, c = queue.pop(0)
                for r_n, c_n in (r+1,c),(r-1,c),(r,c+1),(r,c-1):
                    if (r_n,c_n) not in visited and 0<=r_n<r_max and 0<=c_n<c_max and grid[r_n][c_n]=="1":
                        grid[r_n][c_n]="0"
                        visited.add((r_n, c_n))
                        queue.append((r_n, c_n))
        r, c = 0, 0
        while r<r_max:
            c = 0
            while c<c_max:
                if grid[r][c]=="1":
                    grid[r][c]="0"
                    helper(r,c)
                    res+=1
                c+=1
            r+=1
        return res