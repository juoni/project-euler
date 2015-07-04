# naive recursive fib, in exponential time
def rec_fib(n):
	a = 1
	b = 2
	if (n <= 1):
		return a
	if (n == 2):
		return b
	return rec_fib(n-1) + rec_fib(n-2)

# linear time fib
def it_fib(n):
	a = 1
	b = 2
	if (n <= 1):
		return a
	if (n == 2):
		return b
	while (n > 2): # > 2 b/c because 1st and 2nd fib number have already been
	# computed
		c = a+b # next fib number
		a = b
		b = c
		n -= 1
	return c

# finds the index of the biggest fibonacci number <= lim
def find_limit(lim):
	n = 2
	r = it_fib(n)
	while r < lim:
		n *= 2
		r = it_fib(n)
	while (r >= lim):
		n -= 1
		r = it_fib(n)
	return n

# sums first n even fibonacci numbers
def sol(n):
	a = 1
	b = 2
	s = 2
	if (n <= 1):
		return 0
	if (n == 2):
		return 2
	while (n > 2):
		c = a+b
		if (c % 2) == 0:
			s += c
		a = b
		b = c
		n -= 1
	return s

print "Solution to Project-Euler Problem 2"
#print it_fib(20)
#print rec_fib(20)
print sol(find_limit(4000000))
