#Two Strings: "s" & "t" => if the two strings are anagrams of each other, return True, otherwise False

#Edge case: s="xx" | t = "x"


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = list(s)
        tlist = list(t)
        
        sets = list(set(slist))
        sett = list(set(tlist))
        
        dict1 = {} #Key=letter : Value=count
        dict2 = {}
        #s = xx
        for _set in sets: #for each letter in set list
            dict1[_set] = 0 #Add a key:value=0 pair to the dict
            for letters in slist: #For each letter in set list, iterate over each letter of the unset list
                if _set == letters: #Compare if the set letter is equal to the unset letter
                    dict1[_set] += 1 #If yes, increment dict by one
        print(dict1)
        #s = x
        for _set in sett:
            dict2[_set] = 0
            for letters in tlist:
                if _set == letters:
                    dict2[_set] += 1
        print(dict2)
        if dict1 == dict2:
            return True
        else:
            return False
        