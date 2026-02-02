"""
1. Two Sum
Attempted
Easy
Topics
premium lock icon
Companies
Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

class Solution:
    def twoSum(self, nums: List[int], target: int, verbose: bool = False) -> List[int]:
        dict_hash_map: dict = {}
        index = -1
        for element in nums:
            index = index + 1
            if verbose:
                print("Starting index: ", index)

            # Now checking if the element alredy exists in the hash map (As the dict.update() will not work if key alredy exist)
            # This is the case when target/2 alredy exists in the list
            if element in dict_hash_map.keys():
                if verbose:
                    print("Number found A: ", nums[dict_hash_map[element]], " + ", nums[index], " = ", nums[dict_hash_map[element]] + nums[index])
                    print("Target: ", target)
                    print("*****************")
                return (dict_hash_map[element], index)

            # Checking if the current value in map already
            if len(dict_hash_map) > 1:
                # If value is found then the element already exists in the hash map
                if element in dict_hash_map.keys():
                    if verbose:
                        print("Number found B: ", nums[dict_hash_map[element]], " + ", nums[index], " = ", nums[dict_hash_map[element]] + nums[index])
                        print("Target: ", target)
                        print("*****************")
                    return (dict_hash_map[element], index)
            if verbose:
                print("*****************")

            # Now the case if the element does not exist
            # Assuming the element is one of the solution, storing the complimenting value to check if it occurs
            dict_hash_map.update({target - element: index})
            if verbose:
                print("dict: ", dict_hash_map)


# AI Solution (Way more effective ;p ;p)
class Solution_GPT:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Stores {value_needed: index_of_the_number_that_needs_it}
        needed_values = {}
        
        for i, num in enumerate(nums):
            # Check if the current number is someone else's complement
            if num in needed_values:
                return [needed_values[num], i]
            
            # Otherwise, calculate what number we need to pair with this one
            complement = target - num
            needed_values[complement] = i


nums_array = [3, 2, 4]
target_value = 6
print(Solution().twoSum(nums=nums_array, target=target_value, verbose=False))
