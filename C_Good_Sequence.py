n = int(input())
count = {}
ans = 0
elements = list(map(int, input().split()))
for val in elements:
    if val in count:
        count[val] += 1
    else:
        count[val] = 1

for key, val in count.items():
    if val >= key:
        ans += val - key
    else:
        ans += val

print(ans)