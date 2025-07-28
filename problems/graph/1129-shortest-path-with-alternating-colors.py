"""
Link: https://leetcode.com/problems/shortest-path-with-alternating-colors
Difficulty: medium

Problem:
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. 
Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 
if such a path does not exist.

Input / Output:


Notes:


Solution Approaches:
Breadth first exploration as unweighted graph

"""
class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        # Setup
        graph_red = defaultdict(list)
        graph_blue = defaultdict(list)
        def buildGraph(graph, edges):
            for edge in edges:
                graph[edge[0]].append(edge[1])
        
        # Builds graphs
        buildGraph(graph_blue, blueEdges)
        buildGraph(graph_red, redEdges)

        res = [-1]*n
        visited = set()

        queue = [(0,0,0)]
        while queue:
            curr_node, curr_length, color = queue.pop(0)
            res[curr_node] = curr_length if res[curr_node]==-1 else  min(res[curr_node],curr_length)
            visited.add(curr_node)
            if len(visited)==n: break
            elif color == 0:
                for neighbor in graph_blue[curr_node]:
                    queue.append((neighbor, curr_length+1, 1))
                del graph_blue[curr_node]
                for neighbor in graph_red[curr_node]:
                    queue.append((neighbor, curr_length+1, 2))
                del graph_red[curr_node]
            elif color == 1:
                for neighbor in graph_red[curr_node]:
                    queue.append((neighbor, curr_length+1, 2))
                del graph_red[curr_node]
            elif color == 2:
                for neighbor in graph_blue[curr_node]:
                    queue.append((neighbor, curr_length+1, 1))
                del graph_blue[curr_node]
        
        return res
        