# 2839->다른사람풀이

n = int(input())
sugar = [-1 for i in range(n + 1)]

for i in range(n + 1):
	# print(i, sugar)
	if i < 3 or i == 4: continue # 1,2,4인 경우는 배달x
		
	if i == 3 or i == 5: sugar[i] = 1 # 3, 5 작은 문제 해결
	elif sugar[i-3] == -1 and sugar[i-5] == -1: continue # 작은 문제로 해결이 안되는 경우 pass

	# 큰 문제를 해결해가는 과정
	elif sugar[i-3] == -1: sugar[i] = sugar[i-5] + 1
	elif sugar[i-5] == -1: sugar[i] = sugar[i-3] + 1
	else: sugar[i] = min(sugar[i-5], sugar[i-3]) + 1

# print()
# print(sugar)
print(sugar[n])
