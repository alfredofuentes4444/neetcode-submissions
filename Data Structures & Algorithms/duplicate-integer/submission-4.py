class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty_list = []

        for number in range(len(nums)):
            if nums[number] not in empty_list:
                 empty_list += [nums[number]]
            
            # finds a number twice or more
            else:
                return True
        
        # exits loop
        return False
            