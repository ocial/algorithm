a = str(input())

if len(a) == 1:
    a = '0' + a

b = a[:]

count = 0
while True:
    b = b[-1] + str(int(b[-1]) + int(b[-2]))[-1]

    count += 1
    if b == a:
        break
    
print(count)