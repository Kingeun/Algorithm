#1427
##1
n=int(input())
#a=[]
a=list(map(int,str(n)))
a.sort(reverse=True)

for i in a:
    print(i,end='')
    
    
##2
n = list(input())
n.sort(reverse=True)
print(''.join(n))
