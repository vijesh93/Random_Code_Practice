"""

Code
Testcase
Test Result
Test Result
217. Contains Duplicate
Easy
Topics
premium lock icon
Companies
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
 

"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        print('Start')
                
        # Initializing hash map set
        lookup_map = set()
        
        # Looping around the list
        for item in nums:
            if item in lookup_map:
                return True
            
            else:
                lookup_map.add(item)
        
        return False

class Solution_2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    

if __name__ == "__main__":
    nums_array = [3, 3, 2, 4]
    print(Solution().containsDuplicate(nums=nums_array))
