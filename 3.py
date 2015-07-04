import math
from timeit import default_timer as timer

# determines if prime using trial division
def is_prime(n):
	d = {}
	u = math.floor(math.sqrt(n))
	i = 2
	# trial division: works pretty well for testing 600 billion
	while (i <= u):
		if (n % i == 0):
			return False
		i += 1
	return True

# primality test with sieve
# slower than trial division because it RECOMPUTES SIEVE EVERYTIME for finding
# range of numbers; only faster when cached sieve and checking for many primes;
# better implementation would return a range of prime numbers and use it to
# test primality within that range
def is_prime_sieve(n):
	# first find all prime numbers from 2 to u then test them
	u = math.floor(math.sqrt(n))
	prime = {}
	lst = range(2, int(u)+1)
	for i in lst:
		j = 2
		prime[i] = True
		while (i*j <= u):
			prime[i*j] = False
			j += 1
	while (u >= 2):
		if (u not in prime) or (prime[u]):
			if (n % u == 0):
				return False
		u -= 1
	return True

# observe that 6k+-1 is NOT a O(1) primality test because although that is the
# form of all prime numbers, it is also the form of some composite numbers -
# nevertheless this can help optimize naive trial division. Prime numbers are of
# the form 6k+-1 because all numbers can be represented with 6k+-i where i >= -1
# and <= 4. Factoring out 2 and 3 (because multiples of 2 and 3 are composite)
# eliminates i=0,2,3,4, leaving i=1,-1 To generalize this we can take the
# primorial (factorial with prime numbers) * k instead of 6: c#k. As said
# before, All numbers can be represented with c#k+i as long as i < c#; as c
# grows, we filter out more and more composites in the form of c#k+i (we use the
# primes in the primorial factorial to filter out composite numbers), and
# as c->infinity, we filter out all of them getting something similar to the
# sieve of eratosthenes (we use the multiple of primes in the primorial
# to filter out forms of c#k+i)

# cannot do range(2, largenumber), too much memory taken
# my solution plays on trial division - start with n/=1, then try n/=2, n/=3,
# ..., until prime is found;
# this is because each composite is product of primes; we can get rid of the
# lesser primes by dividing by prime numbers less than largest prime

# returns largest prime factor of n, not largest prime from 2 to n
# faster than O(n), # slower than O(sqrt(n))
def largest_prime_factor(n):
	u = math.floor(math.sqrt(n))
	i = 2
	while (i <= u):
		while (n % i == 0):
			n /= i
		if (is_prime(n)):
			return n
		else:
			i += 1

print "Solution to Project-Euler Problem 3"

#n = 1490000000

#t = timer()
#result = is_prime(n)
#elapsed_time = timer() - t
#print "Trial division primality test returned:", result, "Took:", elapsed_time

#t = timer()
#result = is_prime_sieve(n)
#elapsed_time = timer() - t
#print "Sieve primality test returned:", result, "Took:", elapsed_time

print largest_prime_factor(2309482903581)
print largest_prime_factor(600851475143)

# fundamental theorem of arithmetic: (1) every integer is prime or product of
# primes, and (2) that product is unique (unique number of each prime factor)
# 1. existence proof: p(n) is that for n > 1 n is prime or product of primes.
# base case: p(2) obviously true b/c 2 is prime. inductive hypothesis: p(k), assume
# true that 2 < k < n k is prime or product of primes. inductive step: p(n+1):
# n+1 is either prime or not: if prime, ok cond. satisfied; if not prime, then
# n+1 = ab, where a and b are product of primes. product of product of primes
# generates product of primes. strong induction works because T->T and b/c we
# have base case to ride the hypothesis off of.

# 2. proof that product is unique: let a = q1...qn. if product is not unique
# then also a = p1...pm. However a is divisible by all primes in p1...pm and
# q1...pm. Since p1 is prime, nothing divides it. p1 divides a, and hence
# divides q1...qn. Hence q1 = p1... and we do this for every pm until qn. m =
# n because if either one were bigger it would result in a value bigger than a
