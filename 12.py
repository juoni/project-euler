import sys

# returns nth triangle number
def triangle_number(n):
  if (isinstance(n, int)):
    if (n <= 1):
      sys.exit("triangle_number: n must be > 0")
    else:
      return (n+1)*n/2
  else:
    sys.exit("triangle_number: n must be int")

print triangle_number(7)


