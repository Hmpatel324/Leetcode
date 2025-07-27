"""
Link: https://leetcode.com/problems/all-paths-from-source-to-target
Difficulty: medium

Problem:
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

Input / Output:
graph = [[1,2],[3],[3],[]]
[[0,1,3],[0,2,3]]

Notes:


Solution Approaches:
Basic Breadth First Exploration.
Seed in 0,empty path and terminate when arrive at target node. 

"""
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        # setup
        res = []
        queue = [(0,[])]
        target=len(graph)-1

        # Breadth first exploration
        while queue:
            curr_node, curr_path = queue.pop(0)
            curr_path.append(curr_node)
            if curr_node==target:
                res.append(curr_path)
            else:
                for neighbor in graph[curr_node]:
                    queue.append((neighbor, curr_path[:]))
        return res