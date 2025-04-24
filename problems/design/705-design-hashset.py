"""
Link: https://leetcode.com/problems/design-hashset
Difficulty: easy

Problem:
design hashset

Input / Output:


Notes:


Solution Approaches:
use a dictionary

"""
class MyHashSet(object):

    def __init__(self):
        self.localSet = {}

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.localSet[key] = 1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.localSet.keys():
            del self.localSet[key]

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return key in self.localSet.keys()


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)