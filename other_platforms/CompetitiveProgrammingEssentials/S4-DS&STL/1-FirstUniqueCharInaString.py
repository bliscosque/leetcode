def firstUniqChar(s):
    cnt={}
    for c in s:
        cnt[c]=cnt.get(c,0)+1
    for idx,c in enumerate(s):
        if cnt[c]==1:
            return idx
    return -1

print(firstUniqChar("codingminutes")) # 0
print(firstUniqChar("aabb")) # -1