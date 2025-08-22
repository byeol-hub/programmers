def solution(s):
    answer = ''
    
#     for i in range(len(s)-1):
#         if i == 0:
#             answer += s[i].upper()
#             if s[i] == " " and 'a' <= s[i+1] <= 'z':
#                 answer += s[i+1].upper()
#             else:
#                 answer += s[i+1].lower()
            
#         elif s[i] == " " and 'a' <= s[i+1] <= 'z':
#             answer += s[i+1].upper()
#         else:
#             answer += s[i+1].lower()

    s=s.capitalize()
    
    arr = []
    
    arr = s.split(" ")
    
    for i in arr:
        answer += i.capitalize() + " "
    
    return answer[:-1]