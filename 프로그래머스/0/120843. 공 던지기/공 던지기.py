def solution(numbers, k):
    answer = 0
    
    answer = 2*(k-1) % len(numbers) + 1
    
    return answer