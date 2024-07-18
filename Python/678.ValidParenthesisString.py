class Solution:
    def checkValidString(self, s: str) -> bool:
        options=set()
        options.add(0)

        for ch in s:
            newoptions=set()
            if ch=='(':
                for op in options:
                    newoptions.add(op+1)
            elif ch==')':
                for op in options:
                    if op-1>=0:
                        newoptions.add(op-1)
            elif ch=='*':
                for op in options:
                    newoptions.add(op)
                    newoptions.add(op+1)
                    if op-1>=0:
                        newoptions.add(op-1)
            options=newoptions
        return 0 in options

s=Solution()
print(s.checkValidString("()")) # True
print(s.checkValidString("(*)")) # True
print(s.checkValidString("(*))")) # True
print(s.checkValidString("(")) # False
