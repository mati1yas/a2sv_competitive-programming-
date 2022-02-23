class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        stack = []
        j=0
        long=0
        for i in range (len(s)):
            if s[i] not in stack :
                stack.append(s[i])
                long=max(long,i-j+1)
            else:
                while s[i] in stack:
                    stack.pop(0)
                    j+=1
                stack.append(s[i])
        return long
