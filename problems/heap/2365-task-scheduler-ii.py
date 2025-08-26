"""
Link: https://leetcode.com/problems/task-scheduler-ii
Difficulty: medium>

Problem:
You are given a 0-indexed array of positive integers tasks, 
representing tasks that need to be completed in order, where tasks[i] represents the type of the ith task.

You are also given a positive integer space, 
which represents the minimum number of days that must pass after the completion of a task before another task of the same type can be performed.

Input / Output:


Notes:


Solution Approaches:
keep block on thing that cannot move fwd

"""

import collections
class Solution(object):
    def taskSchedulerII(self, tasks, space):
        """
        :type tasks: List[int]
        :type space: int
        :rtype: int
        """

        counts = collections.Counter(tasks)
        res = 0
        queue = []
        blocking = set()
        res = 0
        while tasks or queue:
            if tasks[0] not in blocking:
                curr_task = tasks.pop(0)
                counts[curr_task]-=1
                if counts[curr_task] > 0:
                    queue.append((curr_task,res+space+1))
                    blocking.add(curr_task)
            res += 1
            if queue and queue[0][1]==res:
                task,time = queue.pop(0)
                blocking.remove(task)
        return res


        