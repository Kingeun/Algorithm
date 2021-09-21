#1193 분수찾기
#1->(1,2)->(3,2,1)->(1,2,3,4)->(5,4,3,2,1)
#1->(2,1)->(1,2,3)->(4,3,2,1)->(1,2,3,4,5)

#1->다른사람
x=int(input())

fra=[] #분자,분모
n=1 #분모

while len(fra) != x:
    if n % 2==1:
        for i in range(n):
            fra.append((n-i,i+1))
            if len(fra)==x:
                break
        n+=1
    else:
        for i in range(n):
            fra.append((i+1,n-1))
            if len(fra)==x:
                break
        n+=1
        
print(str(fra[-1][0])+'/'+str(fra[-1][1]))


#2->다른사람
x=int(input())

num=0  #분모
num_count=0  #분모가 1 증가함에 따라 늘어나는 분수의 갯수

while num_count<x:
    num+=1
    num_count+=num
# print(num, num_count)
num_count -= num # 11번째 줄은 while을 통과하기 위해 불필요하게 계산된 부분이므로 다시 빼줌.


if num % 2 == 0:
    i = x - num_count
    j = num - i + 1
else:
    i = num - (x - num_count) + 1
    j = x - num_count
    

print(f"{i}/{j}")
