class Solution:
    def isValid(self, s: str) -> bool:
        #  valid [ = ]
        # valid ([ = ])

        hashmap = {']': '[',
                    '}': '{',
                    ')': '('
                    }
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            elif char in hashmap:
                if not stack or stack[-1] != hashmap[char]:
                    return False
                stack.pop()
            else:
                return False
        return len(stack) == 0 
        