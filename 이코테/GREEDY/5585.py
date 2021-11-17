# 5585 그리디
n=1000-int(input())
cnt=0
arr=[500,100,50,10,5,1]

for coin in arr:
    cnt+=n//coin
    n%=coin
    
print(cnt)
