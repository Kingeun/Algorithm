#len(arr1)->행의 갯수
#len(arr1[i]->열의 갯수

def solution(arr1, arr2):
    answer = []
    #print(len(arr2))
    #print(len(arr1[0]))
    for i in range(len(arr1)):
        answer.append([])
        
        for j in range(len(arr1[i])):
            answer[i].append(arr1[i][j]+arr2[i][j])
            
    #print(arr1[0])
    return answer
  
  ## https://programmers.co.kr/learn/courses/30/lessons/12950
