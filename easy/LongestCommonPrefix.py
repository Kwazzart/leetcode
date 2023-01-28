from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        triplets = list(zip(*strs))
        sub_str = ""
        for triplet in triplets:
            if len(set(triplet)) == 1:
                sub_str += triplet[0]
                continue
            break
        return sub_str