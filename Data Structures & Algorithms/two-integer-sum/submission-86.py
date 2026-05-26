#Input: array/list: 'nums' | integer: 'target'
#Task: nums[i] + nums[j] == target
#Context: i != j & only one pair of i & j per case


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #Key: Value -> element: index

        for index, element in enumerate(nums):
            required = target - element
            if required in hashmap:
                return sorted([hashmap[required], index])
                break #we dont continue looping and causing more outputs than needed
            else:
                hashmap[element] = index
                continue
        