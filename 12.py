# What is the value of the first triangle number to have over five hundred
# divisors?

import sys
from timeit import default_timer as timer

def time(callback, arg):
  t = timer()
  result = callback(arg)
  elapsed_time = timer() - t
  print "Call took:", elapsed_time

# returns nth triangle number
def triangle_number(n):
  if (isinstance(n, int)):
    if (n <= 1):
      sys.exit("triangle_number: n must be > 0")
    else:
      return (n+1)*n/2
  else:
    sys.exit("triangle_number: n must be int")

# observe that two numbers n and n+1 are coprime (proof: let d|n and d|(n+1),
# then d must divide n-(n+1) (as they are multiples of d). hence gcd(n,n+1)=1
# and the two numbers are coprime). also notice that 1 of the two numbers
# must be even and divisible by 2. multiplying n and n+1 gets us a product of
# primes. the number of divisors is then the result of multiplying all the
# primes' exponents+1 together. must add 1 to exponents before multiplying
# because of zeroth case. this works because all divisors of n(n+1) are the
# product of atleast 1 of the primes that make up n(n+1); multiplying by
# exponents+1 generates all such possibilities. of course for prime 2 we must
# use 2's exponent and not add 1 to it because we divide by 2.

# finds first triangle number with over n divisors
def sol(n):
  i = 1
  prev_divisors = num_divisors(i)
  while (True):
    d = num_divisors(i+1)
    if ((prev_divisors*d) > n):
      print "First triangle number with > n divisors:", i*(i+1)/2
      return
    prev_divisors = d
    i += 1


# modified for sol(), does not return actual num divisors for even numbers
def num_divisors(n):
  count = 1
  exp = 0 # accounts for / 2
  while (n % 2 == 0):
    n = n/2
    exp += 1
  if (exp > 1):
    count *= exp

  exp = 1 # exp + 1
  p = 3
  while (n != 1):
    while (n % p == 0):
      n = n/p
      exp += 1
    if (exp > 1):
      count *= exp
    exp = 1
    p += 2
  return count

time(sol, 500)



