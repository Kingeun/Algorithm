# https://www.acmicpc.net/problem/5639

## 이진 탐색 트리

## 전위 순회 -> 후위 순회!
# 이진 탐색 트리를 이용해서 왼쪽 서브 트리->오른쪽 서브 트리-> 현재 노드 순으로 출력
# 현재 노드보다 작은면 왼쪽 서브 트리, 크면 오른쪽 서브트리로 구분

import sys
sys.setrecursionlimit(10**6)  # 노드에 들어가는 키의 값 제한

# 입력 받을 리스트 데이터 값들 생성
num_list=[]
while True:  # 예외가 발생하기 전까지 입력을 받고 트리에 추가하는 방식
  try:
    num=int(input())
    num_list.append(num)

  except:
    break

# 후위 순회 시작
def postorder(left,right):
  if left>right:
    return
  else:
    mid=right+1   # 큰 원소가 없을 경우를 대비해서 만들었음
    for i in range(left+1,right+1):
      # 해당 원소가 현재 노드보다 크다면 그 전가지 왼쪽 서브 트리
      # 해당 원소 이후에는 오른쪽 서브 트리

      if num_list[left]<num_list[i]:
        mid=i
        break

      postorder(left+1,mid-1)
      postorder(mid,right)  # 순서가 역전되서 종료되도록 함
      print(num_list[left])


postorder(0,len(post)-1)
