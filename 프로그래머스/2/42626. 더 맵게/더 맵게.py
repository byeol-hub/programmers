'''
힙 자료구조를 공부하지 않고 짠 코드로 정확성 테스트는 통과하지만 효율성 테스트는 통과하지 못함
'''

# def solution(scoville, K):
#     answer = 0
#     scoville_min = 0
    
#     scoville.sort()
    
#     if K != 0 and scoville[0] == 0:
#         return -1
    
#     while scoville[0] < K:
#         if len(scoville) == 1:
#             return -1
#         scoville_min = scoville[0] + scoville[1]*2
#         scoville = scoville[2:]
#         scoville.append(scoville_min)
#         answer += 1
#         scoville.sort()
    
#     return answer

def solution(scoville, K):
    answer = 0
    scoville_min = 0
    scoville_heap = []
    
    import heapq
    
    if K != 0 and scoville.count(0) > 1:
        return -1
    
    for i in scoville:
        heapq.heappush(scoville_heap, i)
    
    while scoville_heap[0] < K:
        if len(scoville_heap) == 1:
            return -1
        scoville_min = heapq.heappop(scoville_heap) + heapq.heappop(scoville_heap)*2
        heapq.heappush(scoville_heap, scoville_min)
        answer += 1
    
    return answer

