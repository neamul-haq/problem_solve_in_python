n, m = map(int, input().split())

count = {}
elements = list(map(int, input().split()))
for val in elements:
    if val in count:
        count[val] += 1
    else:
        count[val] = 1

for i in range(1,m+1):
    print(count.get(i, 0))
    
    