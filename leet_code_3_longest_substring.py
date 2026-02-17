"""
3. Longest Substring Without Repeating Characters
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

from ast import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Return the len(s) if single string or None
        if len(s) <= 1:
            return len(s)
        index_end = len(s) - 1
        final_len = 1

        # Hashed string
        window_dict = {s[0]: 0} # Unique characters with index list

        window_end_index = 0
        window_start_index = 0
        while window_end_index < len(s) - 1:

            # Moving the end of the window (increasing to check next)                                  
            window_end_index = window_end_index + 1
            
            # Found character existing in window, then shift the start of the window after the first occurance of the seen character
            # And purge the charcter not in window anymore
            if s[window_end_index] in window_dict.keys() and window_dict[s[window_end_index]] >= window_start_index:
                
                # print("window_start_index before: ", window_start_index)
                window_start_index = window_dict[s[window_end_index]] + 1
                
                # Update the dict: As the new dict should contain the last seen same element.
                # Previous copy of that character is irrelavent
                window_dict[s[window_end_index]] = window_end_index

                window_len = window_end_index - window_start_index + 1
                        
            # Found a character, not in window already
            else:

                # Adding in window_dict and updating window length
                window_dict[s[window_end_index]] = window_end_index
                window_len = window_end_index - window_start_index + 1
                
                # Updating the final length to return
                if final_len < window_len:
                    final_len = window_len
        
        return final_len


class Solution_AI:  # Again more efficient ;p
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_dict = {}
        window_start = 0
        final_len = 0

        for window_end, char in enumerate(s):
            # Check if we've seen this char AND if it's actually in our current window
            if char in window_dict and window_dict[char] >= window_start:
                # Move start to just after the previous occurrence
                window_start = window_dict[char] + 1
            
            # Update the dictionary with the NEW index (no purging needed!)
            window_dict[char] = window_end
            
            # Update max length
            final_len = max(final_len, window_end - window_start + 1)
            
        return final_len

if __name__ == "__main__":
    print('Starting')
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print("Expected: 3 ****************************")
    print(Solution().lengthOfLongestSubstring("bbbbb"))
    print("Expected: 1 ****************************")
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    print("Expected: 3 ****************************")
    print(Solution().lengthOfLongestSubstring(" "))
    print("Expected: 1 ****************************")
    print(Solution().lengthOfLongestSubstring(""))
    print("Expected: 0 ****************************")
    print(Solution().lengthOfLongestSubstring("au"))
    print("Expected: 2 ****************************")

    
    def singleNumber(nums: List) -> int:
        res = 0
        for n in nums:
            res ^= n # XOR each number into res
            # Printing the intermediate result after XORing each number, along with the current number      
            print("After XORing with ", n, " intermediate result is: ", res)
            # print(res, ' n = ', n)
        return res
    
    singleNumber([2, 2, 1, 5, 5, 7, 8, 9, 7, 9, 8]) # Returns 1
    print("Expected: 1 ****************************")
    singleNumber([4,1,2,1,2]) # Returns 4
    print("Expected: 4 ****************************")
