class Solution:
    def interpret(self, command: str) -> str:
        n=len(command)
        ans=""
        i=0
        while i<n:
            if command[i]=='G':
                i+=1
                ans+="G"
            elif command[i]=='(':
                if command[i+1]==')':
                    i+=2
                    ans+="o"
                else:
                    i+=4 
                    ans+="al"
        return ans
    
s=Solution()
print(s.interpret("G()(al)"))