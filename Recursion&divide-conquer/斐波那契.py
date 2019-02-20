def fib_rec(n):
	if n <= 1:
		f = n
	else:
		f = fib_rec(n-1) + fib_rec(n-2)
	return f
if __name__ == '__main__':
	num = 24
	print('fib({0})==>{1}'.format(num,fib_rec(num)))