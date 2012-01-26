# tsp.py traveling salesman problem iterative

global n

def my_key(x):
	num = 0
	for i in range(0,n):
		if ((1<<i)&x) != 0:
			num += 1
	return num
	
if __name__ == '__main__':
	
	f = file('in.data');
	input = f.readline()
	n = (int)(input)
	mat = []
	for i in range(0,n):
		input = f.readline()
		tmpArr = input.split(' ')
		tmpIntArr = []
		for j in range(0,n):
			tmpIntArr.append((int)(tmpArr[j]))
		mat.append(tmpIntArr)
#	for i in range(0,n):
#		print mat[i]
	S = []
	for i in range(1,(1<<n)):
		S.append(i)
#	print S
	S.sort(key = my_key)
#	print S
	while True:
		if S[0] != (1<<(n-1)):
			S.pop(0)
		else:
			S.pop(0)
			break
#	print S
	C = {}			# using dictionary
	C[(1,0)] = 0
#	print C
	for s in S:
		if (s&1) != 0:
#			print s
			C[(s,0)] = 1000000000
			for j in range(1,n):
				for i in range(0,n):
#					print i,' ',j
					if i!=j and ((1<<i)&s) != 0 and ((1<<j)&s) != 0:
						if C.has_key((s,j)):
							if C[(s,j)] > C[(s&(~(1<<j)),i)]+mat[i][j]:
								C[(s,j)] = C[(s&(~(1<<j)),i)]+mat[i][j]
						else:
							C[(s,j)] = C[(s&(~(1<<j)),i)]+mat[i][j]
	res = 1000000000
	for j in range(1,n):
		if res > C[((1<<n)-1,j)] + mat[j][0]:
			res = C[((1<<n)-1,j)] + mat[j][0]
	print res
	f.close()