class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        if not '6' in s:
            return num

        pos=s.find('6')
        s2=s[:pos]+'9'+s[pos+1:]
        return int(s2)

s=Solution()
print(s.maximum69Number(9999)) #9999
print(s.maximum69Number(9669)) #9969
print(s.maximum69Number(9996)) #9999