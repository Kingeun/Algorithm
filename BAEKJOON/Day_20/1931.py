## 1931

'''
강의실 사용 수를 많게 하려면 
1. 강의를 일찍 시작
2. 짧은 강의 시간

'''
n=int(input())
arr=[]

for i in range(n):
    arr.append(tuple(map(int,input().split())))
    
arr=sorted(arr,key=lambda x:x[0]) #시작시간 기준 정렬
arr=sorted(arr,key=lambda x:x[1])  #시작시간이 같으면 끝나는 시간 기준 정렬

answer=[]
for i in arr:
    if len(answer)==0:
        answer.append(i)
        continue
        
    if answer[-1][-1]>i[0]: #다음 수업시간이 이전 수업 시간 끝나는 시간보다 빠를 때

#answer[-1][-1] 이전 수업 시간에서 끝나는 시간
#i[0] 다음 수업시간
        pass
    else:
        answer.append(i)
        
print(len(answer))
