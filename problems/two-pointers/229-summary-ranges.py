"""
Link: https://leetcode.com/problems/summary-ranges
Difficulty: easy

Problem:
Given sorted int list, summarize it using -> notation

Input / Output:
[0,1,2,4,5,7] -> ["0->2","4->5","7"]

Notes:


Solution Approaches:
Accordian expansion 

"""
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        slow, fast = 0,0
        while fast < len(nums):
            # Expansion
            while fast < len(nums)-1 and nums[fast] + 1 == nums[fast+1]:
                fast += 1
            if slow == fast:
                res.append(str(nums[slow]))
            else:
                res.append("%s->%s" % (nums[slow],nums[fast]))
            # Move fwd summary frame
            slow, fast = fast+1, fast+1
        return res