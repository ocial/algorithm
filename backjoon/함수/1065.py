import sys

a = int(sys.stdin.readline().rstrip())

if a <= 99:
    print(a)
elif a <= 110:
    print(99)
else:
    a = range(111, a + 1)
    print(99 + len([n for n in a if n//10%10*2 - n//100 == n%10]))