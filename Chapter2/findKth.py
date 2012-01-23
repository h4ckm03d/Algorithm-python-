# findKth.py

def findKth(arr,k,left,right):
	target = arr[right -1]
	ind = left
	i = left
	while i<right-1:
		if arr[i] <= target:
			tmp = arr[ind]
			arr[ind]=arr[i]
			arr[i]=tmp
			ind+=1
		i+=1
	arr[right-1] = arr[ind]
	if ind-left == k: return target
	elif ind - left > k: return findKth(arr,k,left,ind)
	else : return findKth(arr,k-ind+left-1,ind+1,right)

if __name__ == '__main__':
	arr = [2,1,19, 10, 11 ,100, 5 , 7]
	tmpArr = arr[0:]
	tmpArr.sort()
	print tmpArr
	print arr
	k = int(raw_input('Please input which position you will find(base on 1): '))
	k = k - 1
	if k<0 or k>=len(arr):
		print "I can't find it..."
	else:
		print findKth(arr,k,0,len(arr))