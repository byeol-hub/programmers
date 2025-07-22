def solution(spell, dic):
    answer = 0
    spell_copy = spell.copy()
    
    for i in dic:
        answer = 0
        spell = spell_copy.copy()
        for j in i:
            print(i, j)
            if j in spell:
                spell.remove(j)
                answer += 1
                print(i, answer)
                if answer == len(spell_copy) == len(i):
                    answer = 1
                    return answer
            else:
                break
    
    answer = 2
    
    return answer