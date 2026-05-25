#Given: 1. Array of ints 'nums' | 2. Int 'target'
#Task: Return 2 indexes in the array that add up to the int | Assume every testcase has one correct pair of indexes 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} #val : index

        for index, value in enumerate(nums): #Enumerate allows to iterate through indexes of the list on top
            diff = target - value
            if diff in hashMap:
                return [hashMap[diff], index]
            hashMap[value] = index
        return
        