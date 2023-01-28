class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapper = {"(":")", "[":"]", "{":"}"}
        if s[0] in ["])}", ""]:
            return False

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack or char != mapper[stack.pop()]:
                    return False
        return not stack