#6063
num1,num2=map(int,input().split())
if num1>=num2:
    print(num1)
else :
    print(num2)
    
a, b = input().split()
a = int(a)  #변수 a에 저장되어있는 값을 정수로 바꾸어 다시 변수 a에 저장
b = int(b)
c = (a if (a>=b) else b)
print(int(c))

#6064 삼중항
num1,num2,num3=map(int,input().split())
num=(num1 if num1<num2 else num2) if ((num1 if num1<num2 else num2)<num3) else num3
print(num)

#6065
a,b,c=map(int,input().split())

if a%2==0:
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)
    
#6066
a,b,c=map(int,input().split())
if a%2==0:
    print('even')
else :
    print('odd')
    
if b%2==0:
    print('even')
else :
    print('odd')
    
if c%2==0:
    print('even')
else :
    print('odd')
    
#6067
n=int(input())

if n<0:
    if n%2==0:
        print('A')
    else :
        print('B')
else:
    if n%2==0:
        print('C')
    else:
        print('D')
        
        
#6068
num=int(input())

if 90<=num<=100:
    print('A')
else:
    if num>=70:
        print('B')
    else:
        if num>=40:
            print('C')
        else:
            print('D')
        
     
#6069
eng=input()

if eng=='A':
    print('best!!!')
else:
    if eng=='B':
        print('good!!')
    else :
        if eng=='C':
            print('run!')
        else :
            if eng=='D':
                print('slowly~')
            else:
                print('what?')
                
            
#6070
season=int(input())

if season//3==1:
    print('spring')
else:
    if season//3==2:
        print('summer')
    else:
        if season//3==3:
            print('fall')
        else:
            print('winter')
                    
              
#6071
num=1 #처음 조건 검사를 통과하기 위해 0 아닌 값을 임의로 저장
while num!=0:
    num=int(input())
    if num!=0:
        print(num)
        
        
#6072
num=int(input())
while num!=0:
    print(num)
    num-=1
    
    
#6073
num=int(input())
while num!=0:
    print(num-1)
    num-=1 
    
#알파벳 문자 a의 정수값은 ord('a')로 알아낼 수 있다.
#chr(정수값)을 이용하면 유니코드 문자로 출력할 수 있다.

#6074
eng=ord(input())
t=ord('a')
while t<=eng:
    print(chr(t),end=' ')
    t+=1
    

#6075
num=int(input())
t=0
while t<=num:
    print(t)
    t+=1
    
 
#6076
num=int(input())
for i in range(num+1):
    print(i)
