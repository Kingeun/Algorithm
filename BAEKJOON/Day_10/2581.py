#2581

def prime(n):
    so=0
    for i in range(1,n):
        if n%i==0:
            so += 1
    if so==1:
        return True
    else:
        return False
    
start=int(input())
end=int(input())
b=list(range(start,end+1))
sosu=[]
hap=0

for i in b:
    if prime(i):
        c.append(i)
        hap+=i
        
if len(sosu)==0:
    print(-1)
else:
    print(hap)
    print(min(sosu))
