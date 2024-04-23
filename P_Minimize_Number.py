n = int(input())

elements = list(map(int, input().split()))
ans = 1000000000
for element in elements:
    cnt = 0;
    while element%2==0:
        cnt+=1
        element/=2
    ans = min(ans,cnt)
    
print(ans)