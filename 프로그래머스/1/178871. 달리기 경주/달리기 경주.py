# list.index()로 인해 시간 초과가 남
# list.index(i) 는 리스트에서 i를 처음부터 끝까지 순회하며 찾음 -> O(n)
# callings 배열의 길이만큼 계속 index()를 호출하기 때문에  최악의 경우 시간복잡도가 O(n × m) (n=players 수, m=callings 수)이 됨

# def solution(players, callings):
#     answer = players.copy()
    
#     for i in callings:
#         players = answer.copy()
#         answer[players.index(i)-1] = players[players.index(i)]
#         answer[players.index(i)] = players[players.index(i)-1]
    
#     return answer

def solution(players, callings):
    rank = {player: i for i, player in enumerate(players)} # 선수 이름과 등수를 저장함
    
    for i in callings:
        cur_idx = rank[i] # 현재 등수
        front_idx = cur_idx - 1 # 앞 사람의 등수
        
        front_player = players[front_idx] # 앞 사람의 이름 저장

        players[front_idx], players[cur_idx] = players[cur_idx], players[front_idx] # 순위 교환
            
        rank[i] = front_idx # 앞 사람의 등수 -> 현재 사람의 등수
        rank[front_player] = cur_idx # 현재 사람의 등수 -> 앞 사람의 등수
    
    return players