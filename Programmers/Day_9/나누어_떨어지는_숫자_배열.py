def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor==0:
            answer.append(i)
    if len(answer)==0:
        return [-1]
    else :
        answer=sorted(answer)
        return answer
      
# https://programmers.co.kr/learn/courses/30/lessons/12910?language=python3
