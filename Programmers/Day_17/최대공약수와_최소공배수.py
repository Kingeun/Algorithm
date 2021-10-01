## 다른 사람 풀이

# 1) GCD, LCM using 유클리드 호제법
# 2) math.gcd, math.lcm으로 풀기

def gcd(small, big): # 최대공약수를 찾는 함수!
    if big % small == 0:
        return small
    else:
        return gcd(big % small, small)

def solution(n, m):
    answer = [gcd(n, m), m*n / gcd(n, m)]
    # print(gcd(n, m))
    
    return answer

최대공약수를 찾으면
-> 최소공배수를 간단하게 찾는 공식

두 수를 곱한걸 최대공약수로 나눠주면 -> 최소공배수




78696과 19332의 최대공약수를 찾기
[유클리드 호제법으로 최대공약수 구하기]
78696 ＝ 19332×4 ＋ 1368
19332 ＝ 1368×14 ＋ 180
 1368 ＝ 180×7 ＋ 108
  180 ＝ 108×1 ＋ 72
  108 ＝ 72×1 ＋ 36
   72 ＝ 36×2 ＋ 0
