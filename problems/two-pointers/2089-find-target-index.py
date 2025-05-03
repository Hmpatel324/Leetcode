"""
Link: https://leetcode.com/problems/find-target-indices-after-sorting-array
Difficulty: easy

Problem:
given unsorted list, sort then return indexes that match input target

Input / Output:


Notes:


Solution Approaches:
sort then perform Binary Search 

"""
class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        res = []
        lo, hi = 0, len(nums)-1
        while lo<= hi:
            mid = lo + ((hi-lo)/2)
            if nums[mid]==target and (mid==0 or nums[mid-1] != target):
                while mid<len(nums) and nums[mid]==target:
                    res.append(mid)
                    mid+=1
                return res
            elif nums[mid]<target:
                lo = mid+1
            else:
                hi = mid-1
        return res