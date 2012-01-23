# quickSort.py

def quickSort(arr,left,right):
	if left >= right : return
	ind = left
	target = arr[right-1]
	i=left
	while True:
		if i == right-1: break
		if arr[i] <= target:
			tmp = arr[ind]
			arr[ind] = arr[i]
			arr[i] = tmp
			ind += 1
		i+=1
	arr[right-1]=arr[ind]
	arr[ind]=target
	quickSort(arr,left,ind)
	quickSort(arr,ind+1,right)
	
if __name__ == '__main__':
	arr = [2,1,19, 10, 11 , 19,100, 5 , 7]
	print arr
	quickSort(arr,0,len(arr))
	print arr