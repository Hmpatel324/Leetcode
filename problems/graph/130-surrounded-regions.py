"""
Link: https://leetcode.com/problems/surrounded-regions/
Difficulty: medium

Problem:
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

Input / Output:


Notes:


Solution Approaches:
Breadfirst search and exploration to determine if on edge

"""
class Solution(object):
    def solve(self, grid):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        r_max, c_max = len(grid), len(grid[0])
        visited = set()

        def breadthExploreRegion(r_in,c_in):
            region = set()
            region.add((r_in,c_in))
            queue = [(r_in,c_in)]
            is_on_egde = False
            while queue:
                r,c = queue.pop(0)
                for n_r,n_c in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if n_r<0 or n_r>=r_max or n_c<0 or n_c>=c_max:
                        is_on_egde = True
                        break
                    elif 0<=n_r<r_max and 0<=n_c<c_max and grid[n_r][n_c]=="O" and (n_r,n_c) not in region:
                        region.add((n_r,n_c))
                        queue.append((n_r,n_c))

            # region surrounded so fill with x
            if not is_on_egde:
                for r,c in region:
                    grid[r][c] = "X"
            return region
        
        for i in range(r_max):
            for j in range(c_max):
                if grid[i][j]=="O" and (i,j) not in visited:
                    region = breadthExploreRegion(i,j)
                    visited = visited | region
        return grid