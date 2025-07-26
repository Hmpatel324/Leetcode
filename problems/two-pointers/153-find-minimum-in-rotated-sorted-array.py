"""
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
Difficulty: <difficulty-level>

Problem:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.


Input / Output:
[3,4,5,1,2]
1

[4,5,6,7,0,1,2]
0

Notes:


Solution Approaches:
Binary Search approach. 
Main concept is to determine if you are or are not in a rotated segment

"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo,hi = 0, len(nums)-1
        while lo<hi:
            mid = lo+((hi-lo)/2)
            mid_val = nums[mid]
            if (mid==0 and nums[-1]>nums[mid]): return mid_val
            elif nums[mid-1] > nums[mid]: return mid_val
            elif nums[lo]<=mid_val:
                if nums[hi] < mid_val:
                    lo = mid+1
                else:
                    hi=mid-1
            elif mid_val<nums[hi]:
                if nums[lo] > mid_val:
                    hi = mid-1
                else:
                    lo = mid+1
        return nums[hi]