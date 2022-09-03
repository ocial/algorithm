n = int(input())
m = int(input())
a = list(map(int, input().split()))
a.sort()

count = 0
i = 0
j = n - 1

while i < j:
    sum = a[i] + a[j]
    if sum == m:
        count += 1
        i += 1
        j -= 1
    elif sum < m:
        i += 1
    else:
        j -= 1

print(count)