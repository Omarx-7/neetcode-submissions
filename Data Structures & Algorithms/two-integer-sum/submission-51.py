#Task - Given: 1. array 'nums' 2. int 'target'
#Find the pair inside nums that will add up to target
#intialise hashmap, iterate through each element, conduct calculation, if no match in the hashmap, add and make next comparison

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # Initialise Hashmap
        for index, current in enumerate(nums): #Iterate over both index, and current numbers in the list
            math = target - current #Calculate the second value we are looking for
            if math in hashmap: # is this value already in the hashmap? if so:
                return [hashmap[math], index] #return the value/index of the current/key
            hashmap[current] = index
        return

#4 values: Target, index, current, math
#Hashmap we store the values of the list and its index 
#We compare the math against the values in the dictionary

        