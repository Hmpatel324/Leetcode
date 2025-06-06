"""
Link: https://leetcode.com/problems/clone-graph/
Difficulty: medium

Problem:
Given a node (val, neighbors), deep copy the entire graph

Input / Output:


Notes:


Solution Approaches:
BFS exploration. Keep a store for old:new mapping and a visited set to track what old nodes have been processed.
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return node
        store = {}
        visited = set()
        store[node] = Node(node.val)
        queue = [node]
        while queue:
            curr = queue.pop()
            if curr not in visited:
                visited.add(curr)
                for n in curr.neighbors:
                    if n not in store:
                        store[n] = Node(n.val)
                    store[curr].neighbors.append(store[n])
                    if n not in visited:
                        queue.append(n)
        return store[node]