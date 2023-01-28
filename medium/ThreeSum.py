class Solution:
    def threeSum(self, nums) -> list:
        triplets = []
        sets = set()
        nums = sorted(nums)
        print(nums)
        
        for i in range(len(nums)):
            target = -nums[i]
            l = 0
            r = len(nums)-1
            while l < r:
                if l == i:
                    l += 1
                    continue
                elif r == i:
                    r -= 1
                    continue
                    
                if nums[l] + nums[r] > target:
                    r -= 1
                    
                elif nums[l] + nums[r] < target:
                    l += 1 
                    
                elif nums[l] + nums[r] == target:
                    if frozenset([nums[i], nums[l], nums[r]]) not in sets:
                        sets.add(frozenset([nums[i], nums[l], nums[r]]))
                        triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
        return triplets