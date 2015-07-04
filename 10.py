# sum of primes below 2000000

import math
from timeit import default_timer as timer

# naive solution, check each number from 1 to n for primality
def sum_of_primes_naive(n):
  i = 2
  s = 0
  while i < n:
    if (is_prime(i)):
      s += i
    i+= 1
  return s

# slow sieve
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

# fast sieve, because uses list of bools rather than ints (list of ints slower)
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

def sum_of_primes4(n):
  sieve = [True] * 2000000 # Sieve is faster for 2M primes
  def mark(sieve, x):
      for i in xrange(x*x, len(sieve), x): # can begin at x^2 because x-1 will
      # already have been marked
          sieve[i] = False
  for x in xrange(2, int(len(sieve) ** 0.5) + 1): # only need to check up to
  # sqrt(n), otherwise will encounter duplicate factors
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

# generator for next number to be checked for primality
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

# faster naive version because of space efficiency
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
            for n in xrange(i*i, limit, i):     # can start at i*i because
            # everything before that will already been have marked as false,
            # because if c < i, then any prime < i has its multiples marked,
            # so ci will already be marked. the first multiple of i that will
            # not be marked is the one > c
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
# print space_efficient(2000000) # 77 with 2k+1, 36 with 6k+1!
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
# print sum_of_primes2(2000000) # 69s, 3.35 s using list of booleans; this is
# because the integers took up much more space it seems; what you're storing
# the data in matters
# elapsed_time = timer() - t
# print "Took!:", elapsed_time

# t = timer()
# print sum_of_primes(2000000) # way longer than (2), why? because resizing a
# list is very expensive, must shift all elements down
# elapsed_time = timer() - t
# print "Took:", elapsed_time
