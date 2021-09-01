#6092번
n=int(input())
a=input().split()

for i in range(n):
    a[i]=int(a[i])
    
cnt=[]
for i in range(24):
    cnt.append(0)
    
for i in range(n):
    cnt[a[i]]+=1

for j in range(1,24):
    print(cnt[i],end=' ')
    
    
#6093
n=int(input())
a=input().split()

for i in range(n):
    a[i]=int(a[i])

for i in reversed(range(n)):
    print(a[i],end=' ')
    
#6094
n=int(input())
k=list(map(int,input().split()))
a=k[0]

for i in range(n):
    if a>k[i]:
        a=k[i]
print(a)


#6054
num1,num2 = map(int,input().split())
print(bool(num1) and bool(num2))

#6055
num1,num2 = map(int,input().split())
print(bool(num1) or bool(num2))


#6056
num1,num2=map(int,input().split())
print((bool(num1) and not (bool(num2)) or (not(bool(num1)) and bool(num2))))


#6057
num1,num2=map(int,input().split())
print((bool(num1)) and (bool(num2)) or (not (bool(num1)) and  not (bool(num2))))


#6058
num1,num2=map(int,input().split())
print(not (bool(num1) or bool(num2)))


#6095
d = [] 
for i in range(20): 
    d.append([]) 
    for j in range(20): 
        d[i].append(0) 
        
n = int(input()) 

for i in range(n): 
    x, y = map(int, input().split()) 
    d[x][y] = 1 
    
for i in range(1, 20): 
    for j in range(1, 20): 
        print(d[i][j], end=' ') 
            
    print()
