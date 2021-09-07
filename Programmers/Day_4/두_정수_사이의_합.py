def solution(a,b):
    cnt=0
    if a<b:
        for i in range(a,b+1,1):
            cnt+=i
            #print(cnt)
        return cnt
    elif a>b:
        for i in range(b,a+1,1):
            cnt+=i
            #print(cnt)
        return cnt
        
    else :
        return a
