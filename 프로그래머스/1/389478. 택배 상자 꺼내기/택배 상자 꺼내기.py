# def solution(n, w, num):
#     answer = 0
#     count = 0
#     start = 0
        
#     while start % w != 1:
#         count += 1
#         start = num - count
    
#     print(start, count)
    
#     start = count*2 + 1
#     count = 0
    
#     print(start)
    
#     while True:
#         if (num // w) % 2 == 0:
#             if num + start > n:
#                 break
#             else:
#                 num += start
#                 count += 1
#                 print(num)
#         else:
#             if num + start + w > n:
#                 break
#             else:
#                 num += start + w
#                 count += 1
#                 print(num)
    
#     return count + 1

def solution(n, w, num):
    pos = num - 1
    row = pos // w
    idx = pos % w

    if row % 2 == 0:
        col = idx
    else:
        col = w - 1 - idx

    answer = 1

    max_row = (n - 1) // w

    for r in range(row + 1, max_row + 1):
        if r % 2 == 0:
            box_num = r * w + col + 1
        else:
            box_num = r * w + (w - col)
            
        if box_num <= n:
            answer += 1

    return answer

