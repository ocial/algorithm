# https://programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    answer = sum(int(x) for x in str(number)) + 1
    
    if number % N == 0:
        number = int(number / N)
        answer = sum(int(x) for x in str(number))
    
    if answer > 8:
        answer = -1
        
    return answer


answer = solution(5, 5)
print(answer)



# 1 > 2/2 = 2
# 2 > 2 = 1
# 3 > 2 + 2/2 = 3
# 4 > 2 + 2 = 2
# 5 > 2 + 2 + 2/2 = 4
# 6 > 2 + 2 + 2 = 3
# 7 > 2 + 2 + 2 + 2/2 = 5
# 8 > 2 + 2 + 2 + 2 = 4
# 9 > (22 - 2 - 2) / 2 = 5
# 10 > (22 - 2) / 2 = 4
# 11 > (22) / 2 = 3             1 + 1 + (1)
# 12 > (22 + 2) / 2 = 4         1 + 2 + (1)
# 13 > (22 + 2 + 2) / 2 = 5     1 + 3 + (1)

# 20 > 22 - 2 = 3
# 21 > 22 - 2/2 = 4
# 22 > 22 = 2
# 23 > 22 + 2/2 = 4
# 24 > 22 + 2 = 3
# 25 > 22 + 2 + 2/2 = 5