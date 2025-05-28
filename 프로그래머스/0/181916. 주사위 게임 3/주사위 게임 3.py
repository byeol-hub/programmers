# def solution(a, b, c, d):
#     answer = 0
#     arr = [a,b,c,d]
#     if a == b == c == d:
#         answer = 1111*a
#     elif a != b != c != d != a != c != b != d:
#         answer = min(arr)
#     elif (a==b==c!=d):
#         answer = (10*a+d)**2
#     elif (a==c==d!=b):
#         answer = (10*a+b)**2
#     elif (b==c==d!=a):
#         answer = (10*a+d)**2 
#     elif (a==b==d!=c):
#         answer = (10*a+c)**2
#     elif a==b
#     elif a==b!=c!=d!=a:
#         answer = c*d
#     elif a==c!=b!=d!=a:
#         answer = b*d
#     elif a==d!=b!=c!=a:
#         answer = b*c
#     elif b==d!=a!=c!=b:
#         answer = a*c
#     elif b==c!=a!=d!=b:
#         answer = a*d
#     else:
#         answer = a*b
#     return answer

def solution(a, b, c, d):
    answer = 0
    x = 0
    y = 0
    z = 0
    arr = [a,b,c,d]
    s = set(arr)
    count = len(set(arr))
    if count == 1:
        answer = 1111*a
    elif count == 2:
        for i in arr:
            if i == list(s)[0]:
                x += 1
            elif i == list(s)[1]:
                y += 1
        if x == 2:
            answer=(list(s)[0] + list(s)[1])*abs(list(s)[0] - list(s)[1])
        elif x == 1:
            answer=(10*list(s)[1]+list(s)[0])**2
        else:
            answer=(10*list(s)[0]+list(s)[1])**2
    elif count == 3:
        for i in arr:
            if i == list(s)[0]:
                x += 1
            elif i == list(s)[1]:
                y += 1
            else:
                z += 1
        if x == 2:
            answer=list(s)[1]*list(s)[2]
        elif y == 2:
            answer=list(s)[0]*list(s)[2]
        else:
            answer=list(s)[0]*list(s)[1]
    else:
        answer = min(arr)
    return answer


