# DFS 이용

def dfs(x, y):
    # 넘어간다면
    if x < 0 or x > N - 1 or y < 0 or y > M - 1:
        return False
    # 방문하지 않은 노드라면
    if ice_map[x][y] == 0:
        # 방문한 노드는 얼음으로 만들어서 표시
        ice_map[x][y] = 1
        # 상, 하, 좌, 우 모두 방문해서 함수가 끝나지 않고 모두 방문되었다면
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        # 아이스크림 완성
        return True
    return False

N, M = map(int, input().split())

ice_map = []
for i in range(N):
    ice_map.append(list(map(int, input())))
answer = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            answer += 1
print(answer)
