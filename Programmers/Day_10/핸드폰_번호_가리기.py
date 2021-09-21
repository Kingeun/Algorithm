def solution(phone_number):
    answer=phone_number.replace(phone_number[0:len(phone_number)-4],'*'*(len(phone_number)-4)) 
    
    return answer
  
 
# 다른풀이
def solution(phone_number):
    num_list = list(phone_number)
    
    for i in range(len(num_list) - 4):
        num_list[i] = "*"
        
    total_str = ""
    for i in range(len(num_list)):
        total_str += num_list[i]
    return(total_str)
  
  
  #https://programmers.co.kr/learn/courses/30/lessons/12948?language=python3
