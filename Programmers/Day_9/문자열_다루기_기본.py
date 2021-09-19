def solution(s):
#str.isdigit()메소드는 문자열이 정수를 나타내면 True를 반환.
    if (len(s)==4 or len(s)==6) and s.isdigit()==True:
        return True
    else:
        return False
