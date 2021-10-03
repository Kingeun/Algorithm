## 11047
n,k=map(int,input().split())
cnt=0
arr=[]

for i in range(n):
    arr.append(int(input()))

arr=sorted(arr,reverse=True)
for coin in arr:  
    cnt += k//coin
    k %= coin  # k = k % coin
    
print(cnt)

