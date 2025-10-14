from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
goal = []

for i in range(n):
    if 2 in arr[i]:
        goal = [i, arr[i].index(2)]
        break

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dist = [[-1] * m for _ in range(n)]

queue = deque()
queue.append(goal)
dist[goal[0]][goal[1]] = 0

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            dist[i][j] = 0

for i in range(n):
    for j in range(m):
        print(dist[i][j], end=' ')
    print()
