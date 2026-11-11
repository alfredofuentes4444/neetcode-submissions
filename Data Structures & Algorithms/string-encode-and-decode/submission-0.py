class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        
        for i in range(len(strs)):
            encoded_string += strs[i]
            encoded_string += "*$*"
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        final_output = []
        
        temp_string = ""
        
        for i in range(len(s)):

            temp_string += s[i]

            if temp_string[-3:] == "*$*":
                temp_string = temp_string[:-3]
                final_output += [temp_string]
                temp_string = ""
        
        return final_output