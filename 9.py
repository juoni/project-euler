def sol(n):
  for i in xrange(1, n):
    for j in xrange(i, n):
      if (i+j+((i**2)+(j**2))**.5 == n):
        print i,j
        print i*j *((i**2)+(j**2))**.5

sol (1000)
