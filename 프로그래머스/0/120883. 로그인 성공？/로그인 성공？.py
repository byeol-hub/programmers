def solution(id_pw, db):
    answer = 'fail'
    login_num = 0
    
    for i in range(len(db)):
        if id_pw[0] in db[i]:
            login_num = i
            answer = "wrong pw"
            break
    
    if answer == "wrong pw":
        if id_pw[1] in db[login_num]:
            answer = "login"
    
    return answer