from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for index, value in enumerate(nums):
            hashtable[value] = index
        for index, num in enumerate(nums):
            comp = target - num
            if comp in hashtable and hashtable[comp] != index:
                return [hashtable[comp], index]