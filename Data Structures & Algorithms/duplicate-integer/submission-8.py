class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_array = []

        for i in range(len(nums)):
            if nums[i] not in temp_array:
                temp_array += [nums[i]]
            else:
                return True
        
        return False