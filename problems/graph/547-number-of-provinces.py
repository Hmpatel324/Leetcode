"""
Link: https://leetcode.com/problems/number-of-provinces
Difficulty: medium

Problem:
Find number of islands in a graph

Input / Output:


Notes:


Solution Approaches:
Iterate over graph / explore
On explore, track cities explored and set processed to 0 in graph

"""
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        res = 0
        not_visited = set(range(len(isConnected)))

        def helper(city):
            queue = [city]
            while queue:
                curr = queue.pop(0)
                if curr in not_visited:
                    isConnected[curr][curr] = 0
                    not_visited.remove(curr)
                    for i in range(len(isConnected)):
                        if isConnected[curr][i] == 1:
                            isConnected[curr][i] = 0
                            queue.append(i)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1:
                    res+=1
                    helper(i)
        return res
        