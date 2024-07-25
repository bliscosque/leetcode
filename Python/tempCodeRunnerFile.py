carry2=(ab_xor & carry) << 1
        if carry2:
            ans=ans | carry2
        return ans