from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapper = {}
        for num in nums:
            if num not in mapper:
                mapper[num] = 0
            mapper[num] += 1
            if mapper[num] > 1:
                return True
        return False