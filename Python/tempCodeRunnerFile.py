       first_r=b_right.index('1')
        amt_r=0
        for char in b_right[first_r:]:
            if char=='1':
                amt_r+=1
            else:
                break
        #print(first_r,amt_r)

        if first_l!=first_r:
            return 0
        
        ansst=first_r
        
        ansdiff=abs(first_l-first_r)
        
        ans=0
        for i in range(ansst, ansst+ansdiff):
            ans+=2**(32-ansst-1)
        return ans