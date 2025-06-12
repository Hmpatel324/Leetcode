"""
Link: https://leetcode.com/problems/redundant-connection
Difficulty: medium

Problem:
Find redundant connection in graph

Input / Output:


Notes:


Solution Approaches:
Use union-find algo
Essentially create representative tree for all new connections 
if you find a clash ie both new new_nodes have the same rep then they are in the same tree already and are connected

"""
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent =[i for i in range(len(edges)+1)]
        print(parent)
        def find(node_in):
            if parent[node_in]==node_in:
                return node_in
            return find(parent[node_in])

        
        for e in edges:
            i_r = find(e[0])
            j_r = find(e[1])
            if i_r == j_r:
                return e
            parent[j_r] = i_r