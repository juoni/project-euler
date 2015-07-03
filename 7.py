import math

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

print "Problem 7"
i = 0
j = 2
while (i != 10001):
  if (is_prime(j)):
    i += 1
    print j
  j += 1
