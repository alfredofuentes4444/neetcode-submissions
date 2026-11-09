class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers_dict = {}
        final_nums = []
        counter = 0

        for num in nums:
            if num not in numbers_dict:
                numbers_dict[num] = 0
            numbers_dict[num] += 1

        while counter < k:
            largest_key = None
            largest_count = 0

            for key, value in numbers_dict.items():
                if value > largest_count:
                    largest_key = key
                    largest_count = value

            final_nums += [largest_key]
            del numbers_dict[largest_key]

            counter += 1
        
        return final_nums
            
            