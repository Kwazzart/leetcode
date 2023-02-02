class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''cycle solution'''
        s = s.lower()
        s = [i for i in s if i.isalnum()]
        left = 0
        right = len(s)-1
        while left != len(s):
            if s[right] != s[left]:
                return False
            right -= 1
            left += 1
        return True