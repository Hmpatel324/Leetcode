"""
Link: https://leetcode.com/problems/sort-list
Difficulty: <difficulty-level>

Problem:
Given the head of a linked list, return the list after sorting it in ascending order.

Input / Output: 
head = [4,2,1,3]
[1,2,3,4]

Notes:


Solution Approaches:
create a list dictionary {value: [nodes] }
Then sort the key of the dictionary to determine order then stitch the LL back together
Note edge cases exist for very LAST node (next has to be none) and -1 index for the values as next must be next value[0]

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next: return head
        cache = defaultdict(list)
        while head:
            cache[head.val].append(head)
            head = head.next
        
        res = None
        sorted_keys = sorted(cache.keys())
        for i,v in enumerate(sorted_keys):
            
            if i==len(sorted_keys)-1:
                # cache[v][0].next = None
                for j in range(0,len(cache[v])-1):
                    cache[v][j].next = cache[v][j+1]
                cache[v][-1].next = None
            else:
                if i==0: res = cache[v][0]
                for j in range(0,len(cache[v])-1):
                    cache[v][j].next = cache[v][j+1]
                cache[v][-1].next = cache[sorted_keys[i+1]][0]
        return res
