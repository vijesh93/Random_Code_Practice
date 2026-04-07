"""
15. 3Sum
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Sorting first
        nums_sorted = sorted(nums)

        # Final list
        result = set()

        for i, num in enumerate(nums_sorted):
            
            # IMPORTANT: Check only the right side of the array, as further left tripplets already converd with the left pointer and left i index 
            if i > 0 and nums_sorted[i - 1] == nums_sorted[i]:
                continue
            
            # Initializing pointers
            left_pointer = i
            right_pointer = len(nums) - 1

            while left_pointer < right_pointer:
                
                if i == left_pointer:
                    left_pointer = left_pointer + 1
                    continue
                
                if i == right_pointer:
                    right_pointer = right_pointer - 1
                    continue

                if nums_sorted[left_pointer] + nums_sorted[i] + nums_sorted[right_pointer] == 0:
                    result.add(tuple(sorted([nums_sorted[left_pointer], nums_sorted[i], nums_sorted[right_pointer]])))
                    left_pointer = left_pointer + 1
                
                elif nums_sorted[left_pointer] + nums_sorted[i] + nums_sorted[right_pointer] < 0:
                    left_pointer = left_pointer + 1
                
                else:
                    right_pointer = right_pointer - 1

        return [list(item) for item in result]

