#2775->다른사람풀이
#14층까지 존재
#층수별로 리스트 만들어주기
#[1,2,3,4,5,6,7,8,..]
#[1,3,5,....]

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    apart = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]] #0층/2차원배열
    
    for layer in range(k):
        apart.append([])
        # print(apart)
        # print(layer)
        for room in range(n):
            apart[layer + 1].append(sum(apart[layer][:room + 1]))

    print(apart[-1][-1])
