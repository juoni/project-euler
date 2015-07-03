# fibonacci

# naive exponential
def rec_fib(n):
	a = 1
	b = 2
	if (n <= 1):
		return a
	if (n == 2):
		return b
	return rec_fib(n-1) + rec_fib(n-2)

# linear
def it_fib(n):
	a = 1
	b = 2
	if (n <= 1):
		return a
	if (n == 2):
		return b
	while (n>2):
		c = a+b
		a = b
		b = c
		n-=1
	return c

def find_limit(lim):
	n = 2
	r = it_fib(n)
	while r < lim:
		n *= 2
		r = it_fib(n)
	while (r >= lim):
		n-=1
		r = it_fib(n)
	return n

def sol(n):
	a = 1
	b = 2
	s = 0
	if (n <= 1):
		return a
	if (n == 2):
		return b
	while (n>2):
		c = a+b
		if (c % 2) == 0:
			s += c
		a = b
		b = c
		n-=1
	return s + 2


print "Solution to Project-Euler Problem 2"
#print it_fib(20)
#print rec_fib(20)
print sol(find_limit(4000000))
