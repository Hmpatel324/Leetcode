"""
Link: https://leetcode.com/problems/find-center-of-star-graph
Difficulty: easy

Problem:
Find center node of star graph

Input / Output:


Notes:


Solution Approaches:
Visited Cache
Iterate through edges while checking for collisions
If no collisions then add both nodes in edge to visited

"""
class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        visited = set()
        for edge in edges:
            if edge[0] in visited:
                return edge[0]
            elif edge[1] in visited:
                return edge[1]
            visited.add(edge[0])
            visited.add(edge[1])
        return None