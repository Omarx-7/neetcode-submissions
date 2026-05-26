#Input: Neetcode inputs two things: 1. array/list: 'nums' 2. Integer: 'target'

#Task: Return the indices/indexes of the list in a sorted list: [i, j], such that nums[i] + nums[j] == target and i != j

#Context: 
#1D List. 
#Every input case has exactly one pair of indices/indexes to satisfy the condition. 
#You may not use the same index to satisfy the condition.

#[5, 6, 7, 5]
#Target = 10


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: #self refers to the unique object that the method works with
        hashmap = {} #Initialised Hashmap -> element: Index -> 'in' command always searches the key, thus we search by element
        for index, element in enumerate(nums): #Iterate over index and elements of array
            required = target - element #calculate 2nd value needed to sum w current element to = target 
            if required in hashmap: #If the required value to sum to the 'target' value exists:
                return sorted([hashmap[required], index]) #then return the sorted list of the two indexes which add up to 'target'
                break #Break the loop to prevent any further outputs
            else: 
                hashmap[element] = index #Add the current element's index into the hashmap
                continue #Continue the loop and eventually the hashmap will hold the correct value to sum with current element for target


#Solution Approach
#Optimal Time/Space Complexity comes from iterating over the array only once. Time: O(n) | Space: O()
#1. Initialise Hashmap, then enumerately iterate over list and calculate 2nd value needed w current element in order to sum to 'target'
#2. Check if that calculated value is within the hashmap, if not store it, otherwise output the sorted list.
