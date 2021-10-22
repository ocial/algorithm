# total = list(range(1,101))

# def self_number(a):
#     if a > 100:
#         return
#     else:
#         a += sum(int(num) for num in list(str(a)))
#         try:
#             total.remove(a)
#         except:
#             pass

# for a in total:
#     self_number(a)

# print(*total)

a = range(9999)
test = {*a} - {n + sum(map(int, str(n))) for n in a}
print(*sorted(test))
