#Given: Array of integers (nums) and integer (target)
#Task: nums[i] + nums[j] == target where integer only has one set of solutions. RETURN -> Sorted indexes of the two values in the list


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #Key=num : Value= num's index
        for index, num in enumerate(nums): #Iterate over each value in the list, while taking note of the current index
            required = target - num #What is the value needed to be found in the hashmap
            if required in hashmap: #If required val in hashmap:
                return sorted([hashmap[required], index]) #return the sorted list
                break
            #We add the num NOW in order to make sure we dont compare a current value with itself resultant of it being added prior to checking
            hashmap[num] = index #Add Key:Value pair where Key=num And value= nums index
        return


#for every value in the list
#Calculate the complement number to the current to get the target val
#add current value into the hashmap 
#if the required no is in the hashmap, print required output
#otherwise the loop goes on and we continue
        