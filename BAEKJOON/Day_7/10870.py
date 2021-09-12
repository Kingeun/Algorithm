#10870
def fi(n):
    #for i in range(n):
    if n==0:
        return 0
    elif  n==1:
        return 1
        
    else :
        return fi(n-2)+fi(n-1)
        
n=int(input())
print(fi(n))
