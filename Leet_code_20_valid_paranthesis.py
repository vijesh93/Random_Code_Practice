class Solution:
    def isValid(self, s: str) -> bool:
        
        if s is None:
            return True
        
        open_list = ["(", "{", "["]
        close_list = [")", "}", "]"]
        open_close_dict = {
            "(": ")", 
            "{": "}", 
            "[": "]",
        }
        paranthesis_in_s = []
        
        for character in s:

            if character in open_list:
                paranthesis_in_s.append(character)
            
            if character in close_list:

                # If theere is no open bracets left in the list
                if len(paranthesis_in_s) == 0:
                    return False
                
                # If last close is not same as last open
                if character != open_close_dict[paranthesis_in_s[-1]]:
                    return False

                else:
                    paranthesis_in_s.pop()
        
        # If any unclosed remained
        if len(paranthesis_in_s) != 0:
            return False

        return True


if __name__ == "__main__":
    print(Solution().isValid(r"([])"))
