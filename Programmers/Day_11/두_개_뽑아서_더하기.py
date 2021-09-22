def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
            
    
    #set(answer)
#    while len(answer)>0:
#        if answer[i] == answer[i+1]:
#            del answer[i]

    return sorted(set(answer))


##다른사람 풀이
# 조합으로 풀기
from itertools import permutations

def solution(numbers):
    answer = []
    
    for p in permutations(numbers, 2):
        # print(p)    
        answer.append(sum(p))
    
    return sorted(set(answer))

## https://programmers.co.kr/learn/courses/30/lessons/68644
