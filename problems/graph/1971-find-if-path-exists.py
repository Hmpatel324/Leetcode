"""
Link: https://leetcode.com/problems/find-if-path-exists-in-graph
Difficulty: easy

Problem:
Find if a path exists between a src and dst node

Input / Output:


Notes:


Solution Approaches:
Create Adjacency matrix per node
Start at Src and bfs out and see if dst reached

"""
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if source == destination: return True
        graph = [[] for j in range(0,n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        # BFS
        queue = [source]
        visited = {source}
        while queue:
            curr = queue.pop(0)
            for neighbor in graph[curr]:
                if neighbor == destination:
                    return True
                elif neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return Fals