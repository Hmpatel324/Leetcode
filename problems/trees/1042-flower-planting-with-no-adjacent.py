"""
Link: https://leetcode.com/problems/flower-planting-with-no-adjacent
Difficulty: medium

Problem:
You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] describes a bidirectional path between garden xi to garden yi. 
In each garden, you want to plant one of 4 types of flowers.

All gardens have at most 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden. 
The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.

Input / Output:


Notes:


Solution Approaches:
Modified Breadth First exploration
Create a graph with paths
Seed into Breadth First algo *all* nodes in the graph ie gardens the paths effect

Iterate through and use set subtraction to determine a acceptable candidate flower type

"""
class Solution(object):
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        if not paths: return [1]*n
        flower_types = {1,2,3,4}
        graph = defaultdict(list)
        for edge in paths:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        res = [0]*n
        queue = list(graph.keys())
        while queue:
            curr_node = queue.pop()
            potential_types = flower_types - set()
            for n_garden in graph[curr_node]:
                potential_types -= set() if res[n_garden-1]==0 else {res[n_garden-1]}
            res[curr_node-1] = potential_types.pop()
        
        res = list(map(lambda x: 1 if x==0 else x, res))
        return res
