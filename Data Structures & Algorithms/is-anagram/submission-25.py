#Input: Two strings: 's' & 't'
#Task: If two strings 's' & 't' are anagrams of each other return True, else False.
#Context: s&t are all lowercase


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # O(n) Time
            return False

        hashS, hashT = {}, {} #Space complexity is O(n)

        for i in range(len(s)): #O(n)
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)
        
        return hashS == hashT #Time complexity O(n)
        
#time O(n)
#space O(n)
        




#High Level Approach
#1. We will check if the len of the inputs s and t are the same
#2. Initialise two dictionaries
#
#
#
        