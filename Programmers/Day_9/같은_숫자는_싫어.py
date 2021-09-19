## 참고
def solution(arr):
    answer=[arr[0]] #첫번째 수는 비교할 게 없고 겹치든 안겹치든 무조건 넣어줘야 하므로 처음에 지정    
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            answer.append(arr[i])
        else:
            continue

    return answer
