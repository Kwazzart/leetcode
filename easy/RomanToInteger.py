class Solution:
    def romanToInt(self, s: str) -> int:
        mapper = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        nums = [mapper[i] for i in s]
        result = 0
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                result -= nums[i-1]
            else:
                result += nums[i-1]
        result += nums[-1]
        return result