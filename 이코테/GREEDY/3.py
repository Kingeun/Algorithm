n=int(input())
arr=list(map(int,input().split()))
group=0
cnt=0

arr=sorted(arr)

for i in range(len(arr)):
    cnt+=1
    if cnt>=arr[i]:
        group+=1
        cnt=0
        
print(group)
