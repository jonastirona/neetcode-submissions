class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        pairs = {'(':')', '[':']', '{':'}'}
        for character in s:
            if character in '({[':
                stack.append(character)
            elif len(stack) != 0 and character == pairs[stack[-1]]:
                stack.pop()
            else:
                return False

        return len(stack) == 0
