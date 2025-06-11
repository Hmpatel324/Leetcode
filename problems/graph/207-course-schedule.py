"""
Link: https://leetcode.com/problems/course-schedule
Difficulty: medium

Problem:
Given numCourses / pre-reqs, is it possible to complete all classess

Input / Output:


Notes:


Solution Approaches:
Create DataStruct to account for adjacent neighbors / in degree
Then seed sources and bfs.

"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #Create Data Structure 
        inDegrees = {n:0 for n in range(numCourses)}
        neighbors = {n:[] for n in range(numCourses)}
        sources = set(range(numCourses))
        
        #Parse from prerequisites list
        for edge in prerequisites:
            if(edge[0] in sources):
                sources.remove(edge[0])
            inDegrees[edge[0]]+=1
            neighbors[edge[1]]+=[edge[0]]

        visited = set()
        queue = sources
        while queue: 
            curr = queue.pop()
            if curr not in visited:
                visited.add(curr)
                for n in neighbors[curr]:
                    inDegrees[n]-=1
                    if inDegrees[n]==0:
                        queue.add(n)
        return len(visited)==numCourses
