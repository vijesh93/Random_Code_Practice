from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        range_set = set(range(1, len(nums) + 1))
        
        return list(range_set - nums_set)


if __name__ == "__main__":
    print('Starting')