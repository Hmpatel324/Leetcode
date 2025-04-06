"""
Link: https://leetcode.com/problems/island-perimeter
Difficulty: easy

Problem:
given grid with presence of one single island, return the perimeter

Input / Output:
Grid -> int

Notes:


Solution Approaches:
1. Find seed cell, 2. BFS and determine perimeter

"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        queue = []
        visited = set()
        row_max, col_max  = len(grid), len(grid[0])

        # initial seed cell
        r,c = 0,0
        while r<row_max:
            while c<col_max:
                if grid[r][c] == 1:
                    queue.append((r,c))
                    break
                c+=1
            c = 0
            r+=1
        
        # process island
        while queue:
            r,c = queue.pop(0)
            if not (r,c) in visited:
                visited.add((r,c))
                # neighbors
                neighbors = [(r+1,c), (r-1, c), (r,c-1), (r,c+1)]
                for n_r, n_c in neighbors:
                    if 0 <= n_r < row_max and 0 <= n_c < col_max and grid[n_r][n_c] == 1:
                        if (n_r,n_c) not in visited:
                            queue.append((n_r,n_c))
                    else:
                        res += 1
        return res