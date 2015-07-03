import math
from timeit import default_timer as timer


# determines if prime using trial division
def is_prime(n):
	d = {}
	u = math.floor(math.sqrt(n))
	i = 2
	# trial division: works pretty well for determining 600 billion
	while (i <= u):
		if (n % i == 0):
			return False
		i += 1
	return True

# primality test with sieve
# slower than trial divisin because it RECOMPUTES SIEVE EVERYTIME for finding range of numbers; only faster when cached sieve or checking for many primes
def is_prime_sieve(n):
	# first find all prime numbers from 2 to u
	# then test them
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

# other notes:
# 6k+-1 is NOT a O(1) primality test because althought that is the form of all prime numbers, it is also the form of some composite numbers - nevertheless this can help optimize naive trial division; prime numbers are of form 6k+-1 because all numbers can be represented with 6k+-i where i >= -1 and <= 4
# to generalize this we can take the primorial (factorial with prime numbers) * k instead of 6: c#k. As said before, All numbers can be represented with c#k+i as long as i < c#; as c grows, we filter out more and more composites in the form of c#k+i (we use the primes used in the primorial factorial to filter out composite numbers), and as c->infinity, we filter out all of them getting something similar to the sieve of eratosthenes (because we use the multiple of primes in the primorial to filter out forms of c#k+i)


# returns largest prime factor of n! not largest prime from 2 to n (there is a difference!)
# faster than O(n), slower than O(sqrt(n))
def largest_prime(n):
	u = math.floor(math.sqrt(n))
	i = 2
	while (i <= u):
		while (n%i==0):
			n /= i
		if (is_prime(n)):
			return n
		else:
			i += 1



#	while (d[n] != True):
#		n -= 1
#	return n
#			d[i] = True

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

print largest_prime(2309482903581)
print largest_prime(600851475143)
#print largest_prime(600851475143)

# problem: cannot do range(2, largenumber), too much memory taken
# sol: play on trial division - start with n/1, then try n/2, n/3, ... until prime is found; this is because prime factor is multiplied by another prime to get it, and we can find the largest by starting with the smallest multiplicand


# fundamental theorem of arithmetic: every integer is prime or product of primes, and that product is unique (unique number of each prime factor)
# existence proof: p(n) is that for n > 1 n is prime or product of primes
# - base case: p(2) obviously true b/c 2 is prime
# - inductive hypothesis: p(k), assume true that 2 < k < n k is prime or product of primes
# - inductive step: p(n+1): n+1 is either prime or not: if prime, ok cond. satisfied; if not prime, then n+1 = ab, where a and b are product of primes. product of product of primes generates product of primes.
# strong induction works because T->T and b/c we have base case to ride the hypothesis and step off of

# proof that product is unique. let a = q1...qn. if product is not unique then a = p1...pm. However a is divisible by both p1...pm and q1...pm. Since p1 is prime, nothing divides it. p1 divides a, and hence divides q1...qn. hence q1 = p1... and we do this for every pm until qn. m = n because if either one were bigger it would result in a value bigger than a...
