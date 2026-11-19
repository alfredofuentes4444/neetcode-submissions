class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        notin_array = []

        for i in range(len(nums)):
            if nums[i] not in notin_array:
                notin_array += [nums[i]]
            else:
                return True
        return False