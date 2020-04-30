class Solution:
    def checkValidString(self, s: str) -> bool:
        stack, star_stack = [], []

        for index, p in enumerate(s):
            if p == "(":
                stack.append(index)
            elif p == "*":
                star_stack.append(index)
            else:
                if not stack and not star_stack:
                    return False
                elif stack:
                    stack.pop()
                else:
                    star_stack.pop()

        while stack and star_stack:
            if stack.pop() > star_stack.pop():
                return False
        return not stack