from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answ = []
        L = []
        R = []
        left_val = 1
        right_val = 1
        for i in range(0,len(nums)):
            L.append(left_val)
            R.append(right_val)
            left_val *= nums[i]
            right_val *= nums[len(nums)-i-1]

        R = R[::-1]

        for l, r in zip(L, R):
            answ.append(l*r)

        return answ