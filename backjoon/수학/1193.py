a = int(input())

n = 0
while a > n * (n +  1) / 2:
    n += 1

b = (n * (n + 1) / 2) % a
if n % 2 == 0:
    print(f'{int(n - b)}/{int(1 + b)}')
else:
    print(f'{int(1 + b)}/{int(n - b)}')