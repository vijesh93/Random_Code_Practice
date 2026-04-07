from typing import List


class Solution:
    # BIG HINT:******************************It is just a fabonacci series******************************

    def climbStairs(self, n: int) -> int:

        unique_ways = [0, 1, 2]
        if n <= 2:
            return unique_ways[n]
        
        else:
            for i in range(3, n + 1):
                element = unique_ways[-1] + unique_ways[-2]
                unique_ways.append(element)

        return unique_ways[-1]


class Solution_AI_recurssion:
    
    def climbStairs(self, n: int) -> int:
        # Just add a dictionary to store results!
        memo = {}

        def unique_ways_n(number):
            if number in memo: return memo[number] # Check if we already did the work
            
            if number <= 2:
                return number
            
            # Store the result before returning
            memo[number] = unique_ways_n(number - 1) + unique_ways_n(number - 2)
            return memo[number]

        return unique_ways_n(n)


    if __name__ == "__main__":
        print(Solution().climbStairs(n=20))