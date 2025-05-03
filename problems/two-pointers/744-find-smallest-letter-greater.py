"""
Link: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
Difficulty: easy

Problem:
given ordered list of letters, return next unique after target OR list[0]

Input / Output:


Notes:


Solution Approaches:
binary search

"""
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        target = ord(target)
        lo, hi = 0, len(letters)-1
        while lo <= hi:
            mid = lo + ((hi-lo)/2)
            if ord(letters[mid]) == target:
                while mid+1<len(letters) and ord(letters[mid+1]) == target:
                    mid += 1
                return letters[0] if mid>=len(letters)-1 else letters[mid+1]
            elif ord(letters[mid]) > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return letters[0] if hi==len(letters)-1 else letters[hi+1]