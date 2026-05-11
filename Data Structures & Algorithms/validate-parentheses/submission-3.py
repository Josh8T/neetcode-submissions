class Solution:
    def isValid(self, s: str) -> bool:
        # can never be valid, no closing/opening
        stack = []
        clostToOpen = { ")" : "(", "]": "[", "}": "{"}

        for c in s:
            if c in clostToOpen:
                if stack and stack[-1] == clostToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False


        