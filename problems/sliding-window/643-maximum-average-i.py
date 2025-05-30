"""
Link: https://leetcode.com/problems/maximum-average-subarray-i
Difficulty: easy

Problem:
Find contiguous subarray with largest average

Input / Output:


Notes:


Solution Approaches:
Slide window
Bootstap values then move window until end of list

"""
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        head, tail = 0, k-1
        total = reduce(lambda x,y:x+y, nums[0:k])
        res = total/float(k)
        while tail < len(nums)-1:
            total -= nums[head]
            head+=1
            tail +=1
            total += nums[tail]
            res = max(res, total/float(k))
        return res
