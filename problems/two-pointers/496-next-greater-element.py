"""
Link: https://leetcode.com/problems/next-greater-element-i
Difficulty: easy

Problem:
2 int arrays > transcribe val in list1 to list2 and find next greatest element to right

Input / Output:


Notes:


Solution Approaches:
Pre-process and store as cache then map translate original list

"""
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        cache = {}
        highest = -float('inf')
        nums2 = nums2[::-1]
        for i,v in enumerate(nums2):
            print(v)
            if highest < v:
                cache[v] = -1
            else:
                while i >= 0:
                    if nums2[i] > v:
                        print(nums2[i])
                        cache[v]  = nums2[i]
                        break
                    i-=1
            highest = max(highest, v)
        i = 0
        while i < len(nums1):
            nums1[i] = cache[nums1[i]]
            i+=1
        return nums1
 