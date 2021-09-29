#1011 -> 다른사람풀이
t=int(input())

for i in range(t):
    x,y=map(int,input().split())
    
    d=y-x #거리
    
    cnt=0
    
    while True:
        if d<=cnt*(cnt+1):
            break
        cnt+=1
        
    #총 이동 거리가 n의 제곱보다 작거나 같을 때
    if d<=cnt**2:
        print(2*cnt-1)
    #총 이동 거리가 n의 제곱보다 클 때   
    else:
        print(2*cnt)
        
        
        
# 1011 -> 다른사람풀이

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    n = y - x

    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 0:
        print(0)
    else:
        num = 1
        while True:
            if n <= (num + 1)**2:
                print(2*num + 1)
                break
            if n <= (num + 1)*(num + 2):
                print(2*num + 2)
                break
            num += 1
