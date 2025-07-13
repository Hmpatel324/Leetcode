"""
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
Difficulty: medium

Problem:
Find the index of target - in a potentially rotated list of nums

Input / Output:


Notes:


Solution Approaches:
variation of Binary search
The key is to adjust hi/lo based on if you believe you are in the rotated segment or not

"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo,hi = 0,len(nums)-1
        while(lo<=hi):
            mid = lo+((hi-lo)/2)
            midVal = nums[mid]
            if(midVal == target):
                return mid
            if(nums[lo]<=midVal):
                if(nums[lo]<=target<midVal):
                    hi = mid-1
                else:
                    lo = mid+1
            elif(nums[hi]>=midVal):
                if(midVal<target<=nums[hi]):
                    lo = mid+1
                else:
                    hi = mid-1
        return -1