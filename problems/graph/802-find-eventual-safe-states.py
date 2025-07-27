"""
Link: https://leetcode.com/problems/find-eventual-safe-states
Difficulty: medium

Problem:
There is a directed graph of n nodes with each node labeled from 0 to n - 1. 
The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, 
meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. 
A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. 
The answer should be sorted in ascending order.

Input / Output:


Notes:


Solution Approaches:
Reverse Topolgical search

"""
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        terminal_and_safe_nodes = set()
        incoming = defaultdict(list)
        
        for i,v in enumerate(graph):
            if not v: terminal_and_safe_nodes.add(i)
            else:
                for neighbor in v:
                    incoming[neighbor].append(i)

        queue = list(terminal_and_safe_nodes)

        while queue:
            curr = queue.pop(0)
            for n in incoming[curr]:
                if n not in terminal_and_safe_nodes and not set(graph[n])-terminal_and_safe_nodes:
                    queue.append(n)
                    terminal_and_safe_nodes.add(n)
        return sorted(list(terminal_and_safe_nodes))