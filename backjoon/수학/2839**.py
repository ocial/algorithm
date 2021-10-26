a = int(input())

if a % 5 != 0 and a % 3 != 0 and (a not in {b + c for b in range(0, a, 5) for c in range(0, a, 3)}):
    print(-1)
else:  
    print([((a - x)//5) + x // 3 for x in range(a % 5, a + 1, 5) if x % 3 == 0][0])