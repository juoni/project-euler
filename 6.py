# problem 6: find difference between sum of squares of first n ints, and square of sum of first n ints

import math

# sum of numbers from 1 to n is trivially n*(n+1)/2
def natural_sum(n):
	return n*(n+1)/2.0

# misc: let n^2 be the square of a number, and let (n+1)^2 be the square of a
# number succeeding n. (n+1)^2=n^2+2n+1, meaning that every square of a
# number is greater than its previous square by an odd number, computed with
# the number before it.

# proof that sum of squares = n*(n+1)*(2*n+1)/6.0 is given by the fact that
# summation(1, n, (i+1)^3-(i^3)) simplifies, with its telescoping sum, to
# (n+1)^3-1. The original summation also equals summation(1, n, 3i^2 +
# 3i + 1) = 3*summation(1, n, i^2 + i) + n
# 3*summation(1, n, i^2) + 3(n*(n+1))/2 + n = (n+1)^3 - 1
# 3*summation(1, n, i^2) + 3(n*(n+1))/2 + n = n^3 + 3n^2 + 3n + 1 -1
# 3*summation(1, n, i^2) + 3(n*(n+1))/2 + n = n^3 + 3n^2 + 3n
# 3*summation(1, n, i^2) + (3n^2+3n)/2 = n^3 + 3n^2 + 2n
# 3*summation(1, n, i^2) = (2n^3 + 3n^2 + n)/2
# summation(1, n, i^2) = n*(n+1)*(2*n+1)/6.0

# Solving for  summation i^2 yields the equation.
def sum_of_squares(n):
	return n*(n+1)*(2*n+1)/6.0

print sum_of_squares(10)
print natural_sum(10) ** 2 - sum_of_squares(10)
print natural_sum(100) ** 2 - sum_of_squares(100)
