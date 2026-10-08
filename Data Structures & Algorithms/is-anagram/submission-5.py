class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dict_s, dict_t = {}, {}

        if len(s) != len(t):
            return False
        
        for letter in range(len(s)):
            if s[letter] not in dict_s:
                dict_s[s[letter]] = 0
            if t[letter] not in dict_t:
                dict_t[t[letter]] = 0
            
            dict_s[s[letter]] += 1
            dict_t[t[letter]] += 1
        
        return dict_s == dict_t