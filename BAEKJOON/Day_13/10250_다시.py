# 10250
## 다른사람풀이
t = int(input())
for i in range(t):
	h, w, n = map(int, input().split())

 ## ()
	if n % h == 0:
		y = n // h
		print('%d%02d' % (h, y))
	else:
		x = n % h
		y = n // h + 1

		print('%d%02d' % (x, y))
