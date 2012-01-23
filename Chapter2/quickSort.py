# quickSort.py

def quickSort(arr,right,left):
	if right >= left : return
	ind = right
	target = arr[left-1]
	i=right
	while True:
		if i == left-1: break
		if arr[i] <= target:
			tmp = arr[ind]
			arr[ind] = arr[i]
			arr[i] = tmp
			ind += 1
		i+=1
	arr[left-1]=arr[ind]
	arr[ind]=target
	quickSort(arr,right,ind)
	quickSort(arr,ind+1,left)
	
if __name__ == '__main__':
	arr = [2,1,19, 10, 11 , 19,100, 5 , 7]
	print arr
	quickSort(arr,0,len(arr))
	print arr