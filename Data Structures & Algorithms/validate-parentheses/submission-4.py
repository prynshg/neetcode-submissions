class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pair={
            ')':'(',
            '}':'{',
            ']':'['
        }
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack or stack.pop()!=pair[i]:
                    return False
        
        return len(stack)==0
            