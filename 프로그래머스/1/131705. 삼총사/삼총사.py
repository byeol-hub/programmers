### 내 풀이
def solution(number):
    answer = 0
    
    number.sort()
    
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            for k in range(j+1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    
    return answer

# ### 다른 사람 풀이
# def solution(number):
#     answer = 0
    
#     number.sort()
    
#     from itertools import combinations
    
#     for i in combinations(number, 3):
#         if sum(i) == 0:
#             answer += 1
    
#     return answer