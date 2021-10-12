#1026
n=int(input())
s=[]
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a=sorted(a)
b=sorted(b,reverse=True)

for i in range(len(a)):
    s.append(a[i]*b[i])
    
print(sum(s))
