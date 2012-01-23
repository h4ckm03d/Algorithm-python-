# mergeSort.py recurrsive

def merge(low,mid,high,arr):
	tmpArr = []
	i = low
	j = mid
	while True:
		if i >= mid or j>=high : break
		if arr[i] <= arr[j]:
			tmpArr.append(arr[i])
			i+=1
		else:
			tmpArr.append(arr[j])
			j+=1
	if i < mid:
		while True:
			if i == mid : break
			tmpArr.append(arr[i])
			i+=1
	if j < high:
		while True:
			if j == high : break
			tmpArr.append(arr[j])
			j+=1
	j = 0
	for i in range(low,high):
		arr[i] = tmpArr[j]
		j+=1
	del tmpArr
	
def mergeSort(arr,low,high):
#	print low,' ',high
	if (high - low) == 1: return
	mid = (high + low)/2
	mergeSort(arr,low,mid)
	mergeSort(arr,mid,high)
	merge(low,mid,high,arr)

if __name__ == '__main__':
	arr = [1,4,5,2,3,6]
	print arr
	mergeSort(arr,0,len(arr))
	print arr