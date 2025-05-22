# def solution(my_string, overwrite_string, s):
#     answer = ''
#     if (1 <= len(overwrite_string) <= len(my_string)) and (1 <= len(my_string) <= 1000) and (0 <= s <= (len(my_string) - len(overwrite_string))):
#         n = len(overwrite_string) + s
#         for i in my_string:
#             if i == my_string[s]:
#                 answer += overwrite_string
#                 answer += my_string[n:]
#                 break
#             answer += i
#     return answer

def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]

    
