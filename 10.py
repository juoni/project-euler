# sum of primes below 2000000

import math
from timeit import default_timer as timer

def sum_of_primes3(n):
  lst = range(3, n)
  primes = [2]
  for i in lst:
    k = 0
    for p in primes:
      if (i % p == 0):
        k = 1
        break
    if (k == 0):
      primes.append(i)
  s = 0
  for i in primes:
    s += i
  return s

def sum_of_primes2(n):
    lst = [True] * n
    lst[0] = lst[1] = False
    l = len(lst)
    i = 2
    while i < l:
      if (lst[i] and is_prime(lst[i])):
          j = i * i
          while j < l:
             lst[j] = False
             j += i
      i += 1
    s = 0
    for i in lst:
      if i:
        s += i
    return s

def sum_of_primes_naive(n):
  i = 2
  s = 0
  while i < n:
    if (is_prime(i)):
      s += i
    i+= 1
  return s


def sum_of_primes4(n):
  sieve = [True] * 2000000 # Sieve is faster for 2M primes; what i store data in matters; storing bools instead of ints much faster
  def mark(sieve, x):
      for i in xrange(x*x, len(sieve), x):
          sieve[i] = False

  for x in xrange(2, int(len(sieve) ** 0.5) + 1): # only need to check up to sqrt(n), again, because we all free factors between n will have already been filled up by then...
      if sieve[x]: mark(sieve, x)

  print sum(i for i in xrange(2, len(sieve)) if sieve[i])

def sum_of_primes(n):
    lst = range(2, n)
    l = len(lst)
    i = 0
    while i < l:
      if (is_prime(lst[i])):
          j = i + lst[i]
          while j < l:
             lst.pop(j)
             j += lst[i] - 1
             l -= 1
      else:
        print "should not reach here"
      i += 1
    s = 0
    for i in lst:
      s += i
    return s
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

def next(n):
  k = 1
  i = -1
  num = 6*k+i
  while num < n:
    yield num
    num += 2
    if (-1 == i):
      i = 1
    elif (1 == i):
      i = -1
      k += 1

# faster naive version
def space_efficient(n):
  s = 2+3
  for i in next(n):
    if (is_prime(i)):
      s += i
  return s

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # can start at i*i because everything before that will already been have marked as false, because if c < i, then any prime <i has its multiples marked, so ci will already be marked. the first multiple of i that will not be marked is the one > c
                a[n] = False


t = timer()
print sum_of_primes4(2000000) #.5s
elapsed_time = timer() - t
print "Took:", elapsed_time

t = timer()
print sum(primes_sieve2(2000000)) # 1.35s
elapsed_time = timer() - t
print "Took:", elapsed_time

# t = timer()
# print sum(primes_sieve2(2000000)) # 1.35s
# elapsed_time = timer() - t
# print "Took:", elapsed_time



# t = timer()
# print space_efficient(2000000) # 77 with 2k+1, 36 with 6k+1!
# elapsed_time = timer() - t
# print "Took:", elapsed_time

#lst = range(-21, 20000000)

# t = timer() # pop > indexing, probably because of shifting over array?
# lst.pop(10000000)
# elapsed_time = timer() - t
# print "Took:", elapsed_time


# t = timer()
# b = lst[10000000]
# elapsed_time = timer() - t
# print "Took:", elapsed_time

# t = timer()
# print sum_of_primes3(2000000) # way too long
# elapsed_time = timer() - t
# print "Took:", elapsed_time

# t = timer()
# print sum_of_primes_naive(2000000) # 97
# elapsed_time = timer() - t
# print "Took:", elapsed_time

# t = timer()
# print sum_of_primes2(2000000) # 69 s, 3.35 s using list of booleans; this is because the integers took up much more space it seems; what you're storing the data in matters
# elapsed_time = timer() - t
# print "Took!:", elapsed_time

# t = timer()
# print sum_of_primes(2000000) # way longer than (2), why? because resizing a list is very expensive, must shift all elements down
# elapsed_time = timer() - t
# print "Took:", elapsed_time



print "OK"
