from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for string in strs:
            count = [0]*26
            for char in string:
                count[ord(char)-ord("a")] += 1
            ans[tuple(count)].append(string)

        return ans.values()
        
                