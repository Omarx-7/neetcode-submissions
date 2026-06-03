#Input: Two strings: 's' & 't'
#Task: If two strings 's' & 't' are anagrams of each other return True, else False.
#Context: s&t are all lowercase


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False #If len of both inputs dont equate return False

        hashS, hashT = {}, {} #Two Hashmaps initialised
#       Key=Element:Value=Count

        for i in range(len(s)):
#You cant do hashS[s[i]] += 1 cause you cannot increment a value in the dict when it never existed in the first place
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)

        return hashS == hashT

            





#High Level Approach:
#1. Check if the len of both are the same -> if not return False
#2. initialise two hashmaps
#3. iterate over the range(len) of one of the inputs (repping indexes) and within that:
#4. Per index of the input, add that index into the respective hashmap as a key, with its value +1 per occurance of it
#5. compare both hashmaps (how so?) and return True / False accordingly
        
        