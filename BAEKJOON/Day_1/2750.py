#2750번
n=int(input())
a=[]

for i in range(n):
    a.append(int(input()))
    
#print(a)

b=sorted(a)
for i in range(n):
    print(b[i])
