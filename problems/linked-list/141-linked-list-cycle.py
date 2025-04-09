"""
Link: https://leetcode.com/problems/linked-list-cycle
Difficulty: easy

Problem:
is there cycle in the LL

Input / Output:
head -> boolean

Notes:


Solution Approaches:
Set as a cache for observed, then move along the LL until end or hit a cycle

"""
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cache = set()
        curr = head
        while(curr != None):
            if curr in cache:
                return True
            cache.add(curr)
            curr = curr.next
        return False