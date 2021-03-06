# 1191 트리순회
import sys
input = sys.stdin.readline
n=int(input())
tree=dict()

# 트리 생성하는 과정
# A B C / root left right
for i in range(n):
  root,left,right=input().split()
  tree[root]=[left,right]

#깊이 우선 탐색(DFS)
#깊이 우선 탐색(DFS)은 시작 정점에서부터 특정 경로를 따라 가능한 멀리 있는 정점을 재귀적으로 먼저 방문하는 방식을 의미한다. 
#더 방문할 정점이 존재하지 않으면 다시 뒤로 돌아가 다른 경로를 찾아간다.
# 전위 순회
#1. 현재 노드 값 출력
#2. 현재 노드의 왼쪽 자식의 값이 .이 아니라면 왼쪽 자식으로 이동하고 다시 1번을 진행
#3. 현재 노드의 오른쪽 자식의 값이 .이 아니라면 오른쪽 자식으로 이동하고 다시 1번을 진행
def preorder(v):
  if v!='.':  #자식 노드 있는 경우에만
    print(v,end='') # root 노드 출력
    preorder(tree[v][0]) #왼쪽 노드 탐색
    preorder(tree[v][1]) #오른쪽 노드 탐색
#preorder('C')

# 중위 순회
#1. 현재 노드의 왼쪽 자식의 값이 .이 아니라면 왼쪽 자식으로 이동하고 다시 1번을 진행->.이라면 2번 출력
#2. 현재 노드 값 출력
#3. 현재 노드의 오른쪽 자식의 값이 .이 아니라면 오른쪽 자식으로 이동하고 다시 1번을 진행
def inorder(v):
  if v!='.':
    inorder(tree[v][0])
    print(v,end='')
    inorder(tree[v][1])

#D->B->A->E->C->F->G

# 후위 순회
#1. 현재 노드의 왼쪽 자식의 값이 .이 아니라면 왼쪽 자식으로 이동하고 다시 1번을 진행->.이면 2번 이동
#2. 현재 노드의 오른쪽 자식의 값이 .이 아니라면 오른쪽 자식으로 이동하고 다시 1번을 진행->.이면 3번
#3. 현재 노드 값 출력->다시1로?
def postorder(v):
  if v!='.':
    postorder(tree[v][0])
    postorder(tree[v][1])
    print(v,end='')
#D->B->E->G->F->C->A
preorder('A')
print()
inorder('A')
print()
postorder('A')

# https://kmight0518.tistory.com/24
# https://foxtrotin.tistory.com/187
