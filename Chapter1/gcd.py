#gcd.py

def gcd(a,b):
	if b == 0:
		return a
	else:
		return gcd(b,a%b)

if __name__ == '__main__':
	a = int(raw_input('Please input a: '))
	b = int(raw_input('Please input b: '))
	print gcd(a,b)
