"""
Link: https://leetcode.com/problems/next-greater-node-in-linked-list
Difficulty: medium 

Problem:
output list with value of a index corrisponding to next highest link value

Input / Output:


Notes:


Solution Approaches:
output linklist as a list and iterate backwards

better approach: use a stack / clear out on exploration fwd

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if not head.next: return [0]
        original = []
        curr = head
        while curr:
            original.append(curr.val)
            curr = curr.next
        res = [0]*len(original)
        i = -2
        curr_highest = original[-1]
        while (-1* i) <= len(original):
            if original[i] >= curr_highest:
                res[i] = 0
            else:
                temp = i
                while temp < -1:
                    if original[temp] > original[i]:
                        break
                    temp +=1
                res[i] = original[temp]
            curr_highest = max(curr_highest, original[i])
            i-=1
        return res
