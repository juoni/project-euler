def naive(e):
  n = 2 ** e
  s = 0
  for c in str(n):
    s += int(c)
  print s

naive(1000)
