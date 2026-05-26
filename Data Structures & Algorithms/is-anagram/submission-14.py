#Two Strings: "s" & "t" => if the two strings are anagrams of each other, return True, otherwise False



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = list(s)
        tlist = list(t)
        
        sets = list(set(slist))
        sett = list(set(tlist))
        
        dict1 = {} #Key=letter : Value=count
        dict2 = {}

        for _set in sets: #for each letter in set list
            dict1[_set] = 0 #Add a key:value=0 pair to the dict
            for letters in slist: #For each letter in set list, iterate over each letter of the unset list
                if _set == letters: #Compare if the set letter is equal to the unset letter
                    dict1[_set] += 1 #If yes, increment dict by one
        print(dict1)

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

#Space Complexity = O(m+n) -> There are 3 areas of storage, two which is negligible (set lists and dicts) and one that will take up large
#storage as the two inputs becomes large (s & t list), the space comp is proportional to the sum of the lengths of both strings = m+n

#Time Complexity = O(m+n) -> There are four for loops taking place, two being negligible (set) and the other that will take up time as the
#input becomes large(letters in unset list), thus iterating fully through both unset lists will lead to a time comp of m+n
#REMEMBER the time comp is only m+n as we are bounded by 26 english letters, if it was general characters this would be different

