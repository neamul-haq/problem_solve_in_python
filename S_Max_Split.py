s = input()
l = 0
r = 0
ans = []
empty = ''
for c in s:
    if c=='L':
        l=l+1
    else:
        r=r+1
        
    if l==r:
        empty+=c
        ans.append(empty)
        empty = ''
        l=0
        r=0
    else:
        empty+=c
        
print(len(ans))
for str in ans:
    print(str)