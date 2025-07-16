"""
Link: https://leetcode.com/problems/pacific-atlantic-water-flow/
Difficulty: medium

Problem:
Given a grid, West/North == Pacific and East/Sout == Atlantic
and water flowing only from high to low
Return cells where rain water can flow to both oceans

Input / Output:


Notes:


Solution Approaches:
BFS x2
source for atlantic == row/col -1 and pacific row/col 0

"""
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def bfs(origins,grid,maxR,maxC):
            visited = set()
            queue = origins
            while(queue):
                curr = queue.pop(0)
                if(curr not in visited):
                    visited.add(curr)
                    r,c = curr[0],curr[1]
                    currVal = grid[r][c]
                    for i,j in (r+1,c),(r-1,c),(r,c+1),(r,c-1):
                        if((i,j) not in visited and 0<=i<maxR and 0<=j<maxC and currVal<=grid[i][j]):
                            queue.append((i,j))
            return visited
        
        if(not matrix):
            return matrix
        
        maxR = len(matrix)
        maxC = len(matrix[0])
        
        pac = [(0,n) for n in range(maxC)]+[(n,0) for n in range(maxR)]
        atl = [(n,maxC-1) for n in range(maxR)]+[(maxR-1,n) for n in range(maxC)]
        return list(bfs(pac,matrix,maxR,maxC) & bfs(atl,matrix,maxR,maxC))