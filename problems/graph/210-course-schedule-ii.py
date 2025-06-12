"""
Link: https://leetcode.com/problems/course-schedule-ii
Difficulty: medium

Problem:


Input / Output:


Notes:


Solution Approaches:
Create indgree and neighbors maps
Seed sources (0 indegree)
iterate and decrement indegree until 0
when 0 then add for queue processing

"""
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        inDegree = {i:0 for i in range(numCourses)}
        neighbors = {i:[] for i in range(numCourses)}

        for e in prerequisites:
            inDegree[e[0]]+=1
            neighbors[e[1]].append(e[0])
        
        queue = list(filter(lambda x: inDegree[x]==0, range(numCourses)))
        res = []
        visited = set()
        while queue:
            curr = queue.pop(0)
            if curr not in visited:
                res.append(curr)
                visited.add(curr)
                for n in neighbors[curr]:
                    inDegree[n]-=1
                    if inDegree[n]==0:
                        queue.append(n)
        return res if len(res)==numCourses else []