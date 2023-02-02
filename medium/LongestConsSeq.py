class Solution:
    def longestConsecutive(self, nums) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numSet:
                lenth = 1
                while n+1 in numSet:
                    lenth += 1
                    n += 1
                longest = max(longest, lenth)
        return longest
            
