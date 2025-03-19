"""
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=problem-list-v2&envId=array
Difficulty: easy 

Problem
Essentially given a _sorted_ list of nums, return back the list in place with no duplicates and length

Input / Output:
[1,1,2] => 2 [1,2,_]
[0,0,1,1,1,2,2,3,3,4] => [0,1,2,3,4,_,_,_,_,_]

Notes:
Solution needs to be done in place otherwise would opt to convert to hashset then back to list.
Slow / Fast pointer problem.

Solution Approaches:
Slow should be used to increment writing frame and fast used for searching ahead. 

"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow +=1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1
        