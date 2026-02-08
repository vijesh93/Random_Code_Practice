from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        final_list = []
        for i in range(len(nums)):

            smaller_than_current: int = 0
            for j in range(len(nums)):

                if nums[j] < nums[i]:
                    smaller_than_current = smaller_than_current + 1

            final_list.append(smaller_than_current)
    
        return final_list
    

class Solution_2:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_nums = sorted(nums)
        rank_dict = {}
        len_sorted_nums = len(sorted_nums)
        for i, elem in enumerate(reversed(sorted_nums)):

            rank_dict[elem] = len_sorted_nums - i - 1

        # Final list
        final_list = [rank_dict[item] for item in nums]
        return final_list
        

if __name__ == "__main__":
    print('Starting')
    print(Solution_2().smallerNumbersThanCurrent([8,1,2,2,3]))
    print(Solution_2().smallerNumbersThanCurrent([6,5,4,8]))
    print(Solution_2().smallerNumbersThanCurrent([7,7,7,7]))
    print(Solution_2().smallerNumbersThanCurrent([1,2,3,4,5,6,7,8,9,10]))
    print(Solution_2().smallerNumbersThanCurrent([10,9,8,7,6,5,4,3,2,1]))
    print(Solution_2().smallerNumbersThanCurrent([1,1,1,1,1,1,1,1,1,1]))
    print(Solution_2().smallerNumbersThanCurrent([1,1,1,1,1,1,1,1,1,0]))
    print(Solution_2().smallerNumbersThanCurrent([0,0,0,0,0,0,0,0,0,1]))    
