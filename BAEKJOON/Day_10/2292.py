
# 2292
# 1->6->12->18
n=int(input())
bee=1
cnt=1

while True:
    if bee>=n:
        break
    bee+=6*cnt
    cnt+=1
    
print(cnt)
