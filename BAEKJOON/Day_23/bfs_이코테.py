## BFS 코드구현

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
 
  while queue: # 큐가 빌 때까지 반복
    x, y = queue.popleft()
 
    for i in range(4): # 현재 위치에서 4가지 방향 위치 확인
      nx = x + dx[i]
      ny = y + dy[i]
      # 미로 찾기 공간을 벗어난 경우 무시
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      # 괴물이 있을 경우 무시
      if graph[nx][ny] == 0:
        continue
      # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  
  return graph[n - 1][m - 1] # 가장 오른쪽 아래까지의 최단 거리 반환
 
 
 
n, m = map(int, input().split())
graph = []
 
for i in range(n):
   graph.append(list(map(int, input())))
 
# 이동할 네 가지 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]
 
print(bfs(0,0))
