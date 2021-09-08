#2798
#우선 3개의 조합을 골라서 합을 다 더한 것들을 리스트에 넣은 뒤에 그것들 중에 합이 m을 넘는 값들은 빼고 m을 안넘는 값들중에 가장 큰 값 고르기
from itertools import combinations

n,m=map(int,input().split())
card=map(int,input().split())
blackjack=[]

for i in list(combinations(card,3)):
    com=sum(i)
    if com>m:
        continue
    else:
        blackjack.append(com)
print(max(blackjack))



#2231
n=int(input())


for i in range(n):  #1부터 최대범위까지 모든 경우의 수(브루트 포스)를 처음부터 끝까지 비교
    a=sum(map(int,str(i)))
    #rint(a)
    cnt=i+a
    #print(cnt)
    if cnt==n:
        print(i)
        break
else:
    print(0)
