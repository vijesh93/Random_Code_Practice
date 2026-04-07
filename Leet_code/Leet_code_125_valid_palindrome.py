"""
125. Valid Palindrome
Easy
Topics
premium lock icon
Companies
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)

        # Single alphanum character is always palindrom
        if length == 1:
            return True

        left_pointer = 0
        right_pointer = length - 1
        while left_pointer < right_pointer:

            while not s[left_pointer].isalnum():
                # Only special characters in string
                if left_pointer >= right_pointer:
                    return True
                left_pointer = left_pointer + 1
            
            # Found left charcter to compare
            current_char = s[left_pointer]

            while not s[right_pointer].isalnum():
                # Only special characters in string
                if right_pointer <= left_pointer:
                    return True
                right_pointer = right_pointer - 1
            
            # Found right side character to compare
            complimenting_char = s[right_pointer]

            # If any non similar character comes
            if current_char.lower() != complimenting_char.lower():
                return False
            
            left_pointer = left_pointer + 1
            right_pointer = right_pointer -1
            
        return True


if __name__ == "__main__":
    print('Starting')
    print(Solution().isPalindrome(r"asd4dsa"))

    print(Solution().isPalindrome(r"asd4,dsa"))
    print(Solution().isPalindrome(r"asd4,&$§dsa"))
    print(Solution().isPalindrome(r"asd4,&$  §dsa"))
    print(Solution().isPalindrome(r"A man, a plan, a canal: Panama"))

    # False
    print("****************************")
    print(Solution().isPalindrome(r"asd41dsa"))
