# naive sol for longest chain below n with memoization
def naive(n):
  d = {} # added memoization
  # returns chain length
  def get_chain(x):
    xo = x
    c = 1
    while (x != 1):
      if x in d:
        d[xo] = c + d[x] - 1 # -1 because d[x] also contains 1
        return d[xo]
      if (x % 2 == 0):
        x /= 2
      else:
        x = 3*x + 1
      c += 1
    d[xo] = c
    return c
  i = 2
  l = 1
  li = 2
  while (i < n):
    c = get_chain(i)
    if (c > l):
      l = c
      li = i
    i += 1
  print "Longest chain length is:", l, ", with number:", li

from timeit import default_timer as timer

def time(callback, arg):
  t = timer()
  result = callback(arg)
  elapsed_time = timer() - t
  print "Call took:", elapsed_time

time(naive, 1000000) # ~ 7 sec


