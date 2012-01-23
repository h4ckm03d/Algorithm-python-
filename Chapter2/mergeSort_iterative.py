# mergeSort iterative

def merge(arr1,arr2):
	mid = len(arr1)
	high = len(arr2)
#	print mid,' ',high
	i=0
	j=0
	resArr = []
	while True:
		if i >= mid or j>=high : break
		if arr1[i] <= arr2[j]:
			resArr.append(arr1[i])
			i+=1
		else:
			resArr.append(arr2[j])
			j+=1
	if i < mid:
		while True:
			if i == mid : break
			resArr.append(arr1[i])
			i+=1
	if j < high:
		while True:
			if j == high: break
			resArr.append(arr2[j])
			j+=1
	del arr1
	del arr2
	return resArr

if __name__ == '__main__':
	queue = [[1],[4],[5],[2],[3],[6]] # be care , it's array
#	print queue.pop(0)
#	print queue.pop(0)
	while True:
		if len(queue) == 1: break
		tmp = merge(queue.pop(0),queue.pop(0))
		queue.append(tmp)
	print queue[0],