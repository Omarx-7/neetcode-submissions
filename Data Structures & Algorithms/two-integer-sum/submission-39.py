#Given: 1. Array of ints 'nums' | 2. Int 'target'
#Task: Return 2 indexes in the array that add up to the int | Assume every testcase has one correct pair of indexes 

#Solution: [0 : End] -> [1 : End] -> [2 : End]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexbase = 0
        indexmove = 1
        #Reduce the indexmove by one less than [len(list) - 1] every iteration
        while True:
            if nums[indexbase] + nums[indexmove] == target: #start comparison @ [0] + [1]
                return [indexbase,indexmove] #print current indexes
                break # end the loop after printing output
            else:
                if indexmove == len(nums) - 1: #if indexmove > final index
                    indexbase += 1 #increment base index by 1
                    indexmove = indexbase + 1 #return the comparison for indexmove to compare against the next val
                    continue
                else:
                    indexmove += 1 #if no match increment indexmove by 1 to compare w next val 
                    continue

                    