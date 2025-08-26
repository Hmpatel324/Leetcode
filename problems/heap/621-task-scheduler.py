"""
Link: https://leetcode.com/problems/task-scheduler/
Difficulty: medium>

Problem:
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. 
Each CPU interval can be idle or allow the completion of one task. 
Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

Input / Output:


Notes:


Solution Approaches:
Use heap to pull of highest count every time then shuttle in between a queue.
Queue is used to track when to bring the item back in. 

"""
import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = collections.Counter(tasks)
        queue = []
        heap = [(-v,k) for k,v in count.items()]
        heapq.heapify(heap)

        res = 0
        while heap or queue:
            if heap:
                count, task = heappop(heap)
                if count<-1:
                    queue.append((count+1,task,res+n+1))
            res+=1
            if queue and queue[0][2]==res:
                count, task, time = queue.pop(0)
                heappush(heap,(count,task))
        return res
