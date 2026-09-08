class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()

        return not stack


        '''


        Create an empty stack.
        Go through each character in the string.
        If it is an opening bracket (, {, [, put it into the stack.
        If it is a closing bracket:
        Check if the stack is empty → False.
        Check if the top of the stack matches the closing bracket → if not, False.
        If it matches, remove the top bracket.
        After checking all characters:
        If the stack is empty → True.
        Otherwise → False.


        '''