class Solution:
    def interpret(self, command: str) -> str:
        
        i = 0
        res = ""

        while (i < len(command)):
            if (command[i] == 'G'):
                res += 'G'
            elif (command[i] == '('):
                if ((i+1) < len(command) and (command[i+1] == ')')):
                    res += 'o'
                    i += 1
                elif ((i+3) < len(command) and (command[i+1] == 'a') and (command[i+2] == 'l') and (command[i+3] == ')')):
                    res += 'al'
                    i += 3
            i += 1
        
        return res

obj = Solution()
print(obj.interpret("G()(al)"))