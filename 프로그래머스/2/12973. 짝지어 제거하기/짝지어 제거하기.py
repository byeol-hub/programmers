# def solution(s):
#     answer = 1
#     past = ""

#     while s != "":
#         if past == s:
#             return 0
#         else:
#             past = s[:]
#         for i in range(len(s)-1):
#             if s[i] == s[i+1]:
#                 s = s[:i] + s[i+2:]
#                 break
        
#     return answer

def solution(s):
    answer = 1
    s_stack = [s[0]]
    
    for i in s[1:]:
        if s_stack != [] and s_stack[-1] == i:
            s_stack.pop()
        else:
            s_stack.append(i)
    
    if s_stack != []:
        answer = 0

    return answer