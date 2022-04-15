# DFS 로 구현

size=int(input())
n=int(input())


class Graph():
  def __init__(self,size):
    self.SIZE = size
    self.graph = [[0 for _ in range(size)] for _ in range(size)]

G1=Graph(size)

for _ in range(n):
    u, v = map(int, input().split())

    G1.graph[u-1][v-1]=1
    G1.graph[v-1][u-1]=1


visited = [0 for i in range(size)] #[1 0 0 0 0 0 0]
def dfs(v):
  visited[v-1]=1 #방문
  for i in range(1,size+1):
    if G1.graph[v-1][i-1]==1 and visited[i-1]==0:
      dfs(i)

dfs(1)
cnt=0
for i in range(size):
  if visited[i]==1:
    cnt+=1

print(cnt-1)    # 본인 빼고  
