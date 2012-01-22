#binarySearch.py

def binarySearch(arr,target):
	arr.sort()
	low = 0
	high = len(arr)-1
	while True:
		if low > high: break
		mid = (low+high)/2
#		print "mid : ",mid
		if arr[mid] == target:
			return True
		elif arr[mid] < target:
			low = mid+1
		else:
			high = mid-1
	return False
	
if __name__ == '__main__':
	arr = []
	str = raw_input("Please input the array: ")
	arr = str.split(' ')
	arrInt = []
	arrLen = len(arr)
	for i in range(0,arrLen):
		if arr[i] != '':
			arrInt.append(int(arr[i]))
#	print len(arrInt)
#	print arrInt[0]+arrInt[1]
	target = (int)(raw_input("Please input the search target: "))
	if binarySearch(arrInt,target):
		print "I find it!"
	else:
		print "Sorry..."
#	print arrInt