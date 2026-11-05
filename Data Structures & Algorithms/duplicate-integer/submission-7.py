class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_list = []
        
        for num in nums:
            if num not in temp_list:
                temp_list += [num]
            else:
                return True
        
        return False