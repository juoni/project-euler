from timeit import default_timer as timer
import math

def time(callback, arg):
	t = timer()
	result = callback(arg)
	elapsed_time = timer() - t
	print "Call took:", elapsed_time


# checks for first positive number divsible by numbers from 2 to n
# runtime is in O(n * num/n) = O(n), where n is the max divisor and num is the
# number where full divisibility first occurs
def naive_sol(n):
	divisors = range(2, n+1)
	finished = False
	num = n
	while (not finished):
		for i in divisors:
			if (num % i != 0):
				num += n # small optimization, test only even numbers since even*even
				# is always even... evenness is contagious. to go off of that, test
				# only multiples of n since we know that the solution is a multiple of n
				break
			elif (i == n):
				finished = True
	print "First positive number divisible by 1-" + str(n) + " is:", num

# better sol
# # runtime is in O(n * sqrt(n)), and since n is really small we can do this incredibly fast/ n has to be small because the lcm grows by n! everytime... unless we're interested in calculating for really big numbers.
def better_sol(n):
	a = 3
	res = 2
	while (a <= n):
		res = lcm(res, a)
		a += 1
	print "First positive number divisible by 1-" + str(n) + " is:", res

# multiply all the primes of each number; if a prime occurs in both numbers, take the primes of the number in which they occur the most, and multiply those. why does this work? because we are ensuring that both a and b can be made up of the primes that are being multiplied, we ensure that the result is a multiple of a and b. but how do we know that it is the least? because we take the minimum number of primes needed to make both numbers. we can do this repeatedly for two numbers to get the lcm of multiple numbers - it works because we ensure the minimum number of primes to generate all the numbers each time.
# runtime is around O(max(sqrt(a), sqrt(b))
def lcm(a, b):
	ra = math.floor(a ** .5)
	rb = math.floor(b ** .5)
	i = 2
	m = int(max(ra, rb))
	ca = a
	cb = b

	res = 1
	for i in xrange(2, m+1):
		while (ca % i == 0 or (cb % i == 0)):
			if (ca % i == 0):
				ca /= i
			if (cb % i == 0):
				cb /= i
			res *= i
		if (ca == 1 and cb == 1):
			break
	if (ca != 1):
		res *= ca
	if (cb != 1):
		res *= cb
	return res

# anotehr way to compute LCM: multiply ab, then divide by gcd(a, b). proof: ab is a multiple of a and b. gcd(a,b) is ALL the primes  a and b have in common. ab multiplies all the primes they have together. / by gcd eliminates duplicates of the primes they have in common (hence result should still be divisible by gcd).

# euclidean algorithm proof:
# repeateddly taking remainder a%b and setting that to b, and a to b, will eventually yield b ==0, with a the gcd;
# first prove that the process does generate a 0 in b. we know that each remainder is smaller than the last, and hence if it continues indefinitely it will eventually reach 0. each remainder is smaller than the last because the remainder cannot be greater than what divides it. hence it reduces to zero. let the last equation be bn-1 = bn*qn+1. Then bn-2 = bn-1*qn + bn, meaning bn | bn-2. bn also | bn-1. observe the equation bk = bk+1*qk + bk+2. If d | bk+2 and bk+1, then d | bk. So if an element divides both b's after a b in the sequence, then it divides b also. We can apply this to bn | bn-1 and bn | bn-2. Because bn-3 is made up of bn-2 and bn-1, and because both are divisible by bn, bn-3 is also divisble by bn. We can continue this process indefinitely until a and b is reached. Thus bn | both a and b. Thus bn is a common divisor of both a and b, and bn <= g. To prove that bn is the gcd, consider an arbitary divisor d. d|a and d|b, so a=md and b = nd. Since a=bq+b1, b1=a-bq, so d|b1 also. Continue this inductively and we can see that d|bn. Hence d<=bn. However in our previous proof, we found that bn<=g. Hence d==g==bn, so bn is in fact the gcd!
def gcd(a, b):
	if (b > a):
		c = b
		b = a
		a = c
	if (b == 0):
		return a
	r = a % b
	return gcd(b, r)


# efficient lcm with euclidean
def efficient_lcm(a, b):
	return a*b / gcd(a, b)

# the problem is basically asking smallest number that is multiple of numbers 2-n; one such multiple can be found by multiple all the divisors altogether but that is not always the smallest multiple; in fact the problem is asking for the least common multiple of all the numbers! how to find the least common multiple of 2 numbers?

assert(gcd(105, 252) == 21)
assert(lcm(32, 16) ==  32)
assert(lcm(17, 13) == 17 * 13)
res = time(better_sol, 20) # took < .001 seconds...
#res = time(naive_sol, 20) # 57 seconds runtime

# unique division theorem: given int a, d, where d != 0, there exist UNIQUE int q, r st. a=qd+r where 0<=r<|d|
# two parts to proof:
# 1. proof that given 0<=r. let S={a-nd=r:s.t. n is an int}
# we can let n = -|a|d, then a-(-a)*(d*d) = a+a(d^2), which is a positive number or 0 as long as a>=0 (d can be any integer). hence remainder r can in fact be positive or greater than zero by picking an n =-|a|d
# 2. proof that r < |d|
# by well ordering principle (every subset of nonnegative integers contains a smallest element), we can pick a smallest positive r from S. r=a-nd for some n. Suppose r>=|d| instead of the opposite. Then r-|d| = 0 = a-md, where m=n+1 when d is postiive and n-1 when d is negative. This creates another r=r-d that is nonnegative, meaning that there is another nonnegative number inside S smaller than the r we originally assumed. This contradicts what we assumed, so r<|d|. to show that q and r are unique, suppose q,q1,r,r1 s.t. 0<=r,r1<|d| and a=qd+r and a=q1d+r1. subtracting the equations, we get 0=qd+r-q1d-r1=d(q-q1)+r-r1=0. only possibility of that expression being 0 is q1=q and r1=r, unless d is 0 which is forbidden by the condition!

# proof by contradiciton works because we assume T, and then performa a seriesi of valid operatons on it. if operations performed correctly but still lead to F then T must be false and the opposite must be true instead.
