class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        final_dict = defaultdict(list)

        for word in strs:

            count = [0] * 26

            for letter in word:

                count[ord(letter) - ord("a")] += 1
                
            final_dict[tuple(count)].append(word)

        return list(final_dict.values())

