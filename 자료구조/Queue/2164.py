# 백준 2164

#1) import 사용 x

n=int(input())
que=[]
front=0
rear=n-1

for i in range(n):
  que.append(i+1)  #1부터 시작!
  #que=[1,2,3,4,5,6]

  #1 삭제
  #2 맨 뒤로 3,4,5,6,2
  #3 삭제
  #4 맨 뒤로 5,6,2,4
  #5 삭제
  #6 맨 뒤로 2,4,6
  #2 삭제
  #4 맨 뒤로 6,4
  #6 삭제->끝
  
while rear-front != 0: # 1개 남을 때까지
  front+=1  #삭제->front를 한 칸 뒤로 해서 시작
  que.append(que[front])  # front 숫자 뒤에 삽입

  rear=(rear+1)%len(que) # rear 길이를 늘려주어 숫자 뒤에 삽입한 걸 맞춘다.
  front+=1   # 다음 front로 이동

#[1,2,3,4,5,6] front=1
#[1,2,3,4,5,6,2] rear=7,front=2
#[1,2,3,4,5,6,2] front=3
#[1,2,3,4,5,6,2,4] rear=8,front=4
#[1,2,3,4,5,6,2,4] front=5
#[1,2,3,4,5,6,2,4,6] rear=9.front=6
#[1,2,3,4,5,6,2,4,6] front=7
#[1,2,3,4,5,6,2,4,6,4] rear=10.front=8
#[1,2,3,4,5,6,2,4,6.4] front=9->4출력


print(len(que))
#->while문으로 한번 더 돌아서 11

print(que[front])
print(que[0])
