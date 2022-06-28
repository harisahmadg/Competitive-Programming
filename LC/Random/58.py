class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        lst = s.split()
        return len(lst[-1])
    
    def lengthOfLastWord2(self, s: str) -> int:
        #print(list(range(len(s)-1, -1, -1)))
        c = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                c += 1
            
            if c >= 1 and s[i] == " ":
                return c
        return c

obj = Solution()
print(obj.lengthOfLastWord2("Hello World "))