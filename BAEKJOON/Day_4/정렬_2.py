#1181
n=int(input())
word=[]
for i in range(n):
    a=input()
    word.append(a)
    
word=list(set(word))      
word.sort(key=lambda x : (len(x),x))  #sort의 Key로 활용되는 lambda
for i in word:
    print(i)
    
    
#10814
n=int(input())
member=[]

for i in range(n):
    
    age,name=input().split()
    age=int(age)
    member.append([age,name])
    
member.sort(key=lambda x : x[0])

for i in range(n):
    print(member[i][0],member[i][1])
