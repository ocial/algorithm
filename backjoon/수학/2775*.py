import math

for _ in range(int(input())):
    # k = int(input()) + 1
    # n = int(input())

    # print(int(reduce(lambda x, y: x * y, range(n, n+k)) / factorial(k)))

    k = int(input())
    n = int(input())

    print(math.comb(k+n, k+1))  # 조합
    # print(math.perm(k+n, k+1))  # 순열